Title: Fixing a dead Asus WL-500g
Date: 2010-03-17 10:16
Author: Attila-Mihaly Balazs
Tags: hardware, asus, router, troubleshooting
Slug: fixing-dead-asus-wl-500g
Status: published

A short story with a happy ending: my Asus WL-500g locked up and it
wasn’t starting, even after I hard-reset it (removed the power and
plugged it back in). All the LEDs were constantly on (normally, when you
plug in the power, they should light up for a second or so and the turn
off). After some searching I found [a page on
FixYa](http://www.fixya.com/support/t2474220-assus_wl_500gp_router_hangs)
which pointed me to the following forum thread: [Dead or brick ? Lan and
WAN 1-4 leds on steady](http://wl500g.info/showthread.php?t=11077).
There were a couple of stories here with identical symptoms, so I
decided to give the solution a try.

The tricky part was to find a source which could deliver 2.5A at 5V
(most of the ones I found peaked at 1.5A). Finally I found [this
one](http://www.vitacom.ro/Products/29765/P_SUP_SMP5V2A5/5V-2_5A-SWITCH-ADAPTER-.html)
locally and it worked like a charm! (It seems the trick is to search for
“switch power source”). Also, for extra safety, look carefully at the
adapter when you get it to make sure that it conforms to the
specification (5V DC / 2.5A) and if possible, use a multimeter to ensure
that the polarization is correct (in my case it was + on the inside, –
on the outside).

PS. I didn’t get to disassemble my old source yet, but I will post
photos whenever I do so.
