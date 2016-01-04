Title: The wrong time to update software...
Date: 2011-04-11 16:41
Author: Attila-Mihaly Balazs
Tags: rant, programming
Slug: wrong-time-to-update-software
Status: published

is when the user is the busiest, for example when s/he just started your
application. See for example the screenshot below with Adobe Air (click
trough to see it in its full beauty).

<div class="separator" style="clear: both; text-align: center;">

[![](http://3.bp.blogspot.com/-r_lf3uTwZgY/TaMCg6ba3pI/AAAAAAAADWA/d2bvVKLpVQE/s320/adobe-air-update.png)](http://3.bp.blogspot.com/-r_lf3uTwZgY/TaMCg6ba3pI/AAAAAAAADWA/d2bvVKLpVQE/s1600/adobe-air-update.png)

</div>

The mistakes it makes:

-   It tries to do the update when I'm trying to start Grooveshark (it
    interferes with my intention)
-   It consumes 100% of a core by polling for the presence of running
    applications (I suppose), effectively obliging me to do the update.
    This is combined with frequent releases (which otherwise would be a
    good thing) for maximum annoyance.
-   Although you can't see it in the screenshot, the updater has (had?)
    a bug when it asks for your sudo password: if you misstype it at
    first, then it asks for the root password (which doesn't exists
    under Ubuntu by default) and then it just gets into some weird state
    until the next update is released.

To sum it up: You should download and install the updates in the
background (in a separate, versioned directory, always keeping just the
two most recent versions). Users shouldn't be bothered with this,
*especially when they are trying to get work done!*
