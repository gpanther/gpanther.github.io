Title: Passing UTF-8 trough HTTP
Date: 2013-05-29 20:36
Author: Attila-Mihaly Balazs
Tags: python, PHP, unicode
Slug: passing-utf-8-trough-http
Status: published

These days we should write every code as if it will be used by
international people with a wide variety of personal information (just
look at [Falsehoods Programmers Believe About
Names](http://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/)
for some headscratchers). I would like to do add my small contribution
to this by showing how UTF-8 encoded strings can be passed into GET/POST
parameters.

For this I'll be using the following small PHP script, which can be
quickly run by the [command line PHP
webserver](http://php.net/manual/en/features.commandline.webserver.php)
added in PHP 5.4:

</code>

    GETs: 
    POSTs: 

</code>

We'll test this with the following Python script:

    #!/usr/bin/python
    # vim: set fileencoding=utf-8 :
    import urllib
    import urllib2

    params = {'name': u'東京'}
    params = { k: v.encode('utf-8') for k, v in params.iteritems() }
    data = urllib.urlencode(params)

    url = 'http://localhost:8000/?' + data
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)

    print response.read()

</code>

This all works well and nicely, so here are some conclusions:

-   GET and POST variables need to be UTF-8 encoded after which they
    need to be urlencoded ("% encoded"). See [this StackOverflow
    answer](http://stackoverflow.com/a/1549498/1265).
-   Based on the same answer: hostnames use Punycode instead (but we are
    not concerned with hostnames here)
-   You might need to add the following header for POST requests to
    work: "Content-Type: application/x-www-form-urlencoded;
    charset=UTF-8"
-   Failing to observe this sequence leads to an UnicodeEncodeError in
    urllib.urlencode

