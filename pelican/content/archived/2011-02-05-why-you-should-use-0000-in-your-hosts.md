Title: Why you should use 0.0.0.0 in your hosts file - redux
Date: 2011-02-05 20:50
Author: Attila-Mihaly Balazs
Tags: advertisment, networking
Slug: why-you-should-use-0000-in-your-hosts
Status: published

[![port\_80\_application](http://lh6.ggpht.com/_hrvCBhtWhJ4/TU2cC5oFBAI/AAAAAAAADUQ/Ok_LZtTSurA/port_80_application_thumb%5B11%5D.png?imgmax=800 "port_80_application")](http://lh3.ggpht.com/_hrvCBhtWhJ4/TU2cCPyZ3XI/AAAAAAAADUM/Bhu5tNWwaJM/s1600-h/port_80_application%5B17%5D.png)

Some time ago I (wow, time files!) [I
suggested](http://hype-free.blogspot.com/2009/07/speedy-hosts-blocklists.html)
that using 0.0.0.0 for host-file based blocklists would be faster than
using 127.0.0.1. Above you can see an other reason for using 0.0.0.0:
some applications take up port 80 on the localhost and accessing it can
(potentially) create havoc.

In the example above [TeamViewer](http://www.teamviewer.com/) (which is
quite a nice remote control application BTW – with support for Linux!)
has taken it over and thus it displays a mock page instead of the
advertisement (which is very courteous).

PS. This was also mentioned in the original article, I just wanted to
give an other example.
