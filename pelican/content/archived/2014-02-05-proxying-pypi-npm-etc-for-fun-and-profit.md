Title: Proxying pypi / npm / etc for fun and profit!
Date: 2014-02-05 17:26
Author: Attila-Mihaly Balazs
Tags: npm, mirror, node, javascript, continious integration, python, apache, build, pypi
Slug: proxying-pypi-npm-etc-for-fun-and-profit
Status: published

Package managers for source code (like pypi, npm, nuget, maven, gems,
etc) are great! We should all use them. But what happens if the central
repository goes down? Suddenly all your continious builds / deploys fail
for no reason. Here is a way to prevent that:

Configure Apache as a caching proxy fronting these services. This means
that you can tolerate downtime for the services and you have quicker
builds (since you don't need to contact remote servers). It also has a
security benefit (you can firewall of your build server such that it
can't make any outgoing connections) and it's nice to avoid consuming
the bandwidth of those registries (especially since they are provided
for free).

Without further ado, here are the config bits for Apache 2.4

`/etc/apache2/force_cache_proxy.conf` - the general configuration file
for caching:

    # Security - we don't want to act as a proxy to arbitrary hosts
    ProxyRequests Off
    SSLProxyEngine On
     
    # Cache files to disk
    CacheEnable disk /
    CacheMinFileSize 0
    # cache up to 100MB
    CacheMaxFileSize 104857600
    # Expire cache in one day
    CacheMinExpire 86400
    CacheDefaultExpire 86400
    # Try really hard to cache requests
    CacheIgnoreCacheControl On
    CacheIgnoreNoLastMod On
    CacheStoreExpired On
    CacheStoreNoStore On
    CacheStorePrivate On
    # If remote can't be reached, reply from cache
    CacheStaleOnError On
    # Provide information about cache in reply headers
    CacheDetailHeader On
    CacheHeader On
     
    # Only allow requests from localhost

            Order Deny,Allow
            Deny from all
            Allow from 127.0.0.1


            # Don't send X-Forwarded-* headers - don't leak local hosts
            # And some servers get confused by them
            ProxyAddHeaders Off


    # Small timeout to avoid blocking the build to long
    ProxyTimeout    5

</code>

Now with this prepared we can create the individual configurations for
the services we wish to proxy:

For [pypi](https://pypi.python.org):

    # pypi mirror
    Listen 127.1.1.1:8001


            Include force_cache_proxy.conf

            ProxyPass         /  https://pypi.python.org/ status=I
            ProxyPassReverse  /  https://pypi.python.org/

</code>

For [npm](https://npmjs.org/):

    # npm mirror
    Listen 127.1.1.1:8000


            Include force_cache_proxy.conf

            ProxyPass         /  https://registry.npmjs.org/ status=I
            ProxyPassReverse  /  https://registry.npmjs.org/

</code>

After configuration you need to enable the site (a2ensite) as well as
needed modules (a2enmod - ssl, cache, disk\_cache, proxy, proxy\_http).

Finally you need to configure your package manager clients to use these
endpoints:

For npm you need to edit `~/.npmrc` (or use `npm config set`) and add
`registry = http://127.1.1.1:8000/`

For Python / pip you need to edit `~/.pip/pip.conf` (I recommend having
download-cache as [per Stavros's
post](http://www.stavros.io/posts/faster-installs-with-pip/)):

    [global]
    download-cache = ~/.cache/pip/
    index-url = http://127.1.1.1:8001/simple/

</code>

If you use setuptools (why!? just stop and use pip :-)), your config is
`~/.pydistutils.cfg`:

    [easy_install]
    index_url = http://127.1.1.1:8001/simple/

</code>

Also, if you use buildout, the needed config adjustment in
`buildout.cfg` is:

    [buildout]
    index = http://127.1.1.1:8001/simple/

</code>

This is mostly it. If your client is using any kind of local caching,
you should clear your cache and reinstall all the dependencies to ensure
that Apache has them cached on the disk. There are also dedicated
solutions for caching the repositories (for example
[devpi](http://doc.devpi.net/latest/index.html) for python and
[npm-lazy-mirror](https://npmjs.org/package/npm-lazy-mirror) for node),
however I found them somewhat unreliable and with Apache you have a
uniform solution which already has things like startup / supervision
implemented and which is familiar to most sysadmins.
