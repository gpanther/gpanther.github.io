Title: Screenshot forensics
Date: 2009-11-24 12:48
Author: Attila-Mihaly Balazs
Tags: security, privacy, fun
Slug: screenshot-forensics
Status: published

![2390570910\_09a697ffee\_o](http://lh4.ggpht.com/_hrvCBhtWhJ4/Swu6EThb0wI/AAAAAAAACC4/2uFGOxI_L0I/2390570910_09a697ffee_o%5B2%5D.jpg?imgmax=800 "2390570910_09a697ffee_o")
One of the interesting thing I like to do when reading (security) blog
posts, is to try to deduce details about the machine setup used. You can
find some very interesting tidbits of information, like [Sunbelt using
Symantec AV on some of their
machines](http://hype-free.blogspot.com/2008/01/sunbelt-is-using-symantec-in-house.html).

A couple of current examples:

-   [a CA researcher uses Office 2007 and Google
    Chrome](http://community.ca.com/blogs/securityadvisor/archive/2009/11/22/spam-spam-beware-of-latest-spam-attacks.aspx)
-   a [Sophos researcher seems to prefer
    Ubuntu](http://www.sophos.com/blogs/sophoslabs/?p=7548), or at least
    a Gnome based desktop

If you want to avoid exposing such details, try the following:

<ul>
<li>
Crop the screenshot as much as possible. This has other advantages as
well (smaller image size which leads to quicker display for example)

</li>
<li>
Remember that identification can be done in any number of ways:

</li>
-   Using prominent OS features (like the Mac OS X dock or the Windows
    start menu)
-   Using window “chrome” (title bar, frames, buttons on them, their
    color, etc)
-   Colors and fonts
-   Metadata in the image (if it was edited with [Paint
    .NET](http://www.getpaint.net/) for example, it is very probable
    that it happened on a Windows machine)
-   Never use “blur” or similar effects to hide information, since they
    can be reversed (given that they are completely deterministic)

</ul>
If you are really paranoid, you might want to consider taking the
screenshot on an entirely different OS
([Haiku](http://www.haiku-os.org/) for example :-).

Got fun “screenshot archeology” findings? Share them in the comments!

Picture taken from [DeusXFlorida's
photostream](http://www.flickr.com/photos/8363028@N08/) with permission.
