Title: Setting up IMAP with Yahoo! Mail
Date: 2011-02-22 23:03
Author: Attila-Mihaly Balazs
Tags: email, yahoo, imap
Slug: setting-up-imap-with-yahoo-mail
Status: published

[![Mail
Snail](http://farm5.static.flickr.com/4095/4948726439_c3a632e5f9_t.jpg)](http://www.flickr.com/photos/alecperkins/4948726439/ "Mail Snail by alecperkins, on Flickr")

I'm a long time Yahoo Mail user. Just to illustrate how long I've been
with them: when I joined the space available was a couple of MBs! I
staid with them because I was mostly satisfied (never really caught the
GMail bug), however recently I started looking for options to
consolidate the different email accounts (work / personal / yahoo /
gmail / etc). I explicitly wanted IMAP support because I really need to
keep in sync between multiple machines.

The common wisdom seems to be on the 'net that Yahoo! Mail doesn't
support IMAP (not even for paid accounts) or that various hacks are
needed to support it (like sending custom / non-standard commands after
login). This information however seems to be outdated, since I was able
to find a least 3 IMAP servers (I've tested them all and they all work -
with standard email clients with no hacks!):

-   imap.mail.yahoo.com (this is the one Thunderbird configures by
    default)
-   winmo.imap.mail.yahoo.com (from this
    [article](http://www.withinwindows.com/2011/01/31/yahoo-confirmed-culprit-in-windows-phone-data-usage-overages/))
-   zimbra.imap.mail.yahoo.com

All of the servers support SSL/TLS encryption, so they are safe to
access even from public hotspots. The outgoing server is
smtp.mail.yahoo.com, which also supports SSL/TLS (and you should use
it!)

The easiest to set up is Mozilla Thunderbird, however Evolution seems to
work much better. One important feature in particular is that it works
with large (10 000+ emails) folders, while Thunderbird chokes with an
error ("UNAVAILABLE] UID FETCH too many messages in request"). To have
Evolution work properly, you need to select "IMAP+" (also called IMAPX)
as the protocol.

HTH somebody out there.
