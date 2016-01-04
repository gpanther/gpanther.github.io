Title: Upgrading the Options (GlobeTrotter) GI515m
Date: 2011-10-08 15:55
Author: Attila-Mihaly Balazs
Tags: hardware, orange, windows, modem, networking
Slug: upgrading-options-globetrotter-gi515m
Status: published

Recently I needed to install an Options (GlobeTrotter) GI515m 3G USB
modem on a machine which previously used an older version of the modem
(the iCON 225). This seems a pretty common scenario (an existing user
getting an update), however the process seems less-than-straight
forward:

1.  Get a second computer with the same operating system version which
    didn't have a 3G modem installed (for example if your target system
    is running Windows 7 64 bit you need a second system with Windows 7
    64 bit - different skews like Home vs Ultimate are ok, but the
    version and "bitness" must coincide - you could also try using a
    virtual machine for the second machine which supports USB forwarding
    like VirtualBox or VMWare)
2.  Plug in the modem in the second machine. First it will recognize it
    as an USB stick / CD-ROM. Copy all the files from it to a separate
    folder (you should see files like "`setup.exe`").
3.  Let the setup complete. Now copy the installed drivers to the same
    place you've saved setup file. Under Windows 7 you would find them
    in the location `C:\Windows\System32\DriverStore\FileRepository\` in
    several folders starting with "gth" (like
    `gthsubus_64.inf_amd64_neutral_4810563f34b37ef5`), but here is the
    generic way to identify the folder:
    1.  Start Device Manager
    2.  Look for one of the devices associated with the modem (you will
        find actually several, like GlobeTrotter GI515M - Modem
        Interface, Network Interface and so on)
    3.  Properties -\> Driver -\> Driver Details. Note the name of the
        driver for which the provider is Option (for example
        `gtuhsser.sys`)
    4.  Now search your Windows folder for files ending in .inf which
        contain the name of driver from the previous step. This will
        point you to the right folders

4.  On the first computer (the one you actually want to install the
    modem on) remove all previous versions of the software using the
    Add-Remove Programs facility (you will see two-three entries but
    they can be easily identified by the same orange icon). Restart the
    computer for good measure.
5.  Copy over the setup program and the drivers from the second
    computer. Plug in the modem to the first computer, install the
    application (using the setup file captured on the second computer).
    Go into the device manager and look for "Unknown device"s (you
    should see four of them). Use the drivers captured on the second
    computer to resolve these issues.
6.  Unplug and replug the modem - it now should work!

A couple more talking points:

-   don't use "driver manager" type software - they very rarely (read:
    never) seem to work
-   a symptom that you've hit this problem is when the management
    interface (dialer / "Internet Everywhere") for the modem starts but
    it gets stuck in the "Initializing" phase when you connect the modem
    and consumes CPU (from what I've seen with a debugger it seems to be
    looking for the installed device in a loop)
-   the modem seems to be prone to overheating if the signal-strength is
    low (around two bars) and in this case it shuts down after \~10
    minutes (I assume that this is some kind of thermal protection). You
    can check if this is the case by putting your hand on the bottom
    side of the modem. I couldn't find and solution for this, other than
    looking for a spot which has better signal. Using the modem in EDGE
    rather than 3G mode also seems to do the trick, but it has lower
    speeds and I don't know of any reliable method to make the modem use
    EDGE if 3G is also available.

