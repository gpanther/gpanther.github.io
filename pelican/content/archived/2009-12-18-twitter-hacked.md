Title: Twitter hacked
Date: 2009-12-18 13:16
Author: Attila-Mihaly Balazs
Tags: security, hack, deface, twitter, web
Slug: twitter-hacked
Status: published

<div style="float: right;">

<script type="text/javascript"><br />
    slashdot_url="http://hype-free.blogspot.com/2009/12/twitter-hacked.html";<br />
</script>
<script src="http://slashdot.org/slashdot-it.js" type="text/javascript"></script>

</div>

<div style="float: right; clear: right; margin-top: 1em;">

<a class="DiggThisButton">
![DiggThis](http://digg.com/img/diggThis.png)</a>
<script src="http://digg.com/tools/diggthis.js" type="text/javascript"></script>

</div>

It had to happen, didn’t it? I’ve fired up
[Pidgin](http://www.pidgin.im/) with the
[microblog-purple](http://code.google.com/p/microblog-purple/) plugin,
only to get an “invalid certificate” error for twitter. I’ve quickly
became nervous, since a quick digging indicated that I was getting the
wrong IP address for the domain twitter.com.

My first thought was: “I’ve been compromised”. After quickly verifying
my hosts file and my DNS entry, all seemed fine on the surface. My
second thought was: “my DNS server was compromised”, so I’ve done the
same lookup using OpenDNS and the new Google DNS, both coming up with
different (but wrong) answers. Finally I’ve checked out a couple of
other HTTPS sites and they seemed fine. So I took a deep breath and
(putting my faith in [NoScript](http://noscript.net/) and
[RequestPolicy](http://www.requestpolicy.com/)) visited twitter.com to
find the following page:

![twitter\_hack](http://lh4.ggpht.com/_hrvCBhtWhJ4/SyssNIUA3aI/AAAAAAAACEE/XW1kUzm_yg4/twitter_hack%5B6%5D.png?imgmax=800 "twitter_hack")

Quick analysis:

-   This seems to be a “good old” defacement
-   A very likely scenario is that they somehow compromised the DNS
    registrar account (phising, dumb password reset, etc) and changed it
    to point to an other IP.
-   Currently I’m seeing a couple of different IPs out there for the
    twitter.com domain:
    -   My DNS server (and OpenDNS) returns
        [66.147.242.88](http://domaintools.com/66.147.242.88)
    -   Google DNS returns
        [74.217.128.160](http://whois.domaintools.com/74.217.128.160)
-   The correct address seems to be
    [168.143.171.84](http://whois.domaintools.com/twitter.com), so if
    you put the following line in your host file, thing should start
    working again (you might need to do an `ipconfig /flushdns` if
    you're on Windows):

        168.143.171.84 twitter.com

-   The above is a hackish solution, and I would recommend using it only
    in life-and-death situations :-p. It is the best to let Twitter
    handle the incident and make sure that everything is cleaned up.
-   It is unclear when exactly the defacement happened, but it must have
    been in the last 10 hours or so. It might have been specifically
    targeted so that it is late in the day in the USA so that the
    reaction is delayed.
-   ~~According to [Google Translate](http://translate.google.com/#)
    ([Babelfish](http://babelfish.yahoo.com/) doesn’t know Arabic
    unfortunately) the text below the picture says:~~

    Ok, so I'm a big ignorant idiot. The official language of Iran is
    [Persian](http://en.wikipedia.org/wiki/Persian_language) (also known
    as Farsi or Parsi), not Arabic. Thank you to Anonymous for pointing
    it out. According to [this
    article](http://www.mirror.co.uk/news/top-stories/2009/12/18/twitter-hacked-by-iranian-protesters-115875-21907173/)
    the text in the picture says:

    > This site has been hacked by the Iranian Cyber Army (on the flag)

    and

    > The USA thinks they control and manage internet access, but they
    > don't. We control and manage the internet with our power, so do
    > not try to incite the Iranian people (under the picture)

    Some people also seem to have screenshots with English texts on
    them.

-   The rogue server doesn’t seem to respond to any Twitter API
    requests, so it doesn’t seem to be that they were going after
    usernames and passwords (which they very well might have done,
    considering the number of users who click trough SSL certificate
    warnings), but just to be on the safe side, *change your password*
    and *don’t use the same password on all the sites*!

*Update*: As of now all seems to be back to normal and all the DNS
servers return the correct IP address. I’m waiting for an explanation in
Twitter (mostly because I’m interested in how it happened :-)).

*Update*: [Twitter acknowledges the
hack](http://blog.twitter.com/2009/12/dns-disruption.html) on their blog
and say that they will provide more information as it becomes available
(however they erroneously affirm that the API were working correctly –
they weren’t, since they used the same DNS record to contact Twitter –
in fact this is how I’ve became aware of the hack).

Bonus: what sources can you use to investigate such incidents?

-   First of all, be suspicious of SSL certificate errors! I know that
    they (sadly) are quite common these days, but be vigilant!
-   Check that the problem is not at your end. Check that you have the
    correct DNS server (there are a couple of malware families out there
    which set a custom DNS server for the machine to control the users
    browsing destinations). Check that the given hostname is not present
    in your hosts file (again, there are a couple of malware families
    using this method to misdirect users)
-   Check what the IP address should be, by using
    [domaintools](http://whois.domaintools.com/twitter.com) for example
    (and looking at the server stats page)
-   Try looking up the DNS name using several DNS servers (this might
    not work if your network filters DNS queries):

        # nslookup
        > set type=ANY
        > twitter.com
        ...
        > server 8.8.8.8
        > twitter.com
        ...
        > server 208.67.222.222
        > twitter.com
        ...

-   An other option is to use the [vURL
    service](http://vurl.mysteryfcm.co.uk/?url=1160923) to fetch the
    suspicious webpage from different location and compare the results
    with what you are seeing.

Using these methods you can quickly ascertain with pretty good accuracy
where the fault lies and take appropriate action. Have a safe holiday
everybody!

*Update*:

-   Read about the subject on [the TrendMicro Countermeasures
    Blog](http://countermeasures.trendmicro.eu/twitter-not-hacked-by-iranian-cyber-army/).
-   Some more links to information and the source of the defaced webpage
    at [Hacker News](http://news.ycombinator.com/item?id=1002640).
-   SANS [posted about in
    issue](https://isc.sans.org/diary.html?storyid=7774) in the diary.
-   I've update the translations, thanks to Anonymous
-   Twitter [posted an
    update](http://blog.twitter.com/2009/12/update-on-last-nights-dns-disruption.html)
    about the issue. It doesn't many more details, it does however give
    a timeframe for the problem: between 21:46 and 23:00 PST . There are
    some rumors out there that somehow (phising?) the correct password
    to the DNS management interface was obtained and it was used to
    modify the records. Twitter still has the original blogpost up
    saying that API's were not affected, but *this is not true*! If
    you've used a third party Twitter client and you've clicked trough
    the certificate warning (or maybe it doesn't use TLS at all), your
    password might have been compromised. Currently there is no evidence
    that the rogue server was logging passwords, but until the time some
    forensics is done on it, there is no sure way to tell if this was
    the case (since it is trivial to configure a webserver such that it
    responds with a 404 error, while still logging the details of the
    request).
-   Arbor Networks [posted a related
    article](http://asert.arbornetworks.com/2009/12/your-dns-is-an-asset-twitter-dns-woes/).
-   Sucuri has also [posted about the
    issue](http://blog.sucuri.net/2009/12/twitter-defacement.html). They
    have a nice little network monitoring / alerting system. You can
    also use them as [a third-party information
    source](http://sucuri.net/index.php?page=scan&scan=www.twitter.com).
-   ISS X-Force (part of IBM) has also [a nice writeup about the
    incident](http://blogs.iss.net/archive/dnsresolution.html).
-   Brian Krebs has [an informative
    writeup](http://voices.washingtonpost.com/securityfix/2009/12/twittercom_hijacked_by_iranian.html?wprss=securityfix)
    on the SecurityFix blog about the issue which quotes Dyn's (the host
    for the Twitter DNS) CTO as saying: "Someone logged in who purported
    to be a legitimate user of their [DNS] platform account and started
    making changes", further strengthening the probability that a
    Twitter employee's email account was broken into via some mechanism.
-   There is also a lot of confusion out there, as it always is the case
    with (security) news. I've heard someone saying that "why did the
    DNS host allow the redirection of Twitter to a host in Iran?" - just
    to clarify: even though the hack was claimed by the "Iranian Cyber
    Army" (which might not mean anything! it could be your nerdy
    neighbor), the server it was redirected to was in the US.

![3036343674\_54b4674f93\_b](http://lh6.ggpht.com/_hrvCBhtWhJ4/SytP_Yh5udI/AAAAAAAACEM/HwP5a7SjhWw/3036343674_54b4674f93_b%5B7%5D.jpg?imgmax=800 "3036343674_54b4674f93_b")

Picture taken from [pugetsoundphotowalks'
photostream](http://www.flickr.com/photos/25636851@N03/) with
permission.
