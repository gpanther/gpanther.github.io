Title: Manually enabling IP routing in Windows XP
Date: 2011-02-06 11:37
Author: Attila-Mihaly Balazs
Tags: windows, networking
Slug: manually-enabling-ip-routing-in-windows
Status: published

While Internet Connection Sharing is a nifty tool, there are some cases
where you would like to do the steps manually. One such case would be if
the “primary” network is already using the 192.168.0.1/24 address space,
since ICS is hardcoded (as far as I can tell) to use the same network.
One concrete case I have encountered was:

`ADSL Modem+Router (no wireless) –-> laptop broadcasting over writess –-> ... –-> other laptops`

The solution is the following:

-   Set up an ad-hoc network on laptop wifi card (using a different
    subnet – 10.0.0.0/24 for
    example)[![wireless-network-setup](http://lh3.ggpht.com/_hrvCBhtWhJ4/TU5rtQ6LazI/AAAAAAAADU0/SooFF6rYhIE/wireless-network-setup_thumb%5B2%5D.png?imgmax=800 "wireless-network-setup")](http://lh5.ggpht.com/_hrvCBhtWhJ4/TU5rsO2uxwI/AAAAAAAADUw/MkhnLDzuvRs/s1600-h/wireless-network-setup%5B4%5D.png)
-   “Connect” to it to make it
    work:[![wireless-network](http://lh6.ggpht.com/_hrvCBhtWhJ4/TU5ru8_YhcI/AAAAAAAADU8/4pzk87-wpw0/wireless-network_thumb%5B3%5D.png?imgmax=800 "wireless-network")](http://lh3.ggpht.com/_hrvCBhtWhJ4/TU5ruIg4-kI/AAAAAAAADU4/DSyFrIZ8s-M/s1600-h/wireless-network%5B5%5D.png)
-   [Enable IP forwarding on the machine from the
    registry](http://technet.microsoft.com/en-us/library/cc962461.aspx)

It is simple as 1-2-3 :-p. Some caveats though:

-   This setup won’t give you DHCP. So make sure that you configure your
    other machines with a static IP address
-   It also won’t give you DNS, so configure something like the Google
    DNS (8.8.8.8 or 8.8.4.4) or OpenDNS (208.67.222.222 or
    208.67.220.220) or even your ISPs DNS
-   The ad-hoc wifi connection has reliability issues. It happened
    multiple times that I had to restart it because it disconnected and
    wouldn’t connect any more, but it is a good temporary solution.

PS. You can download the drivers and user manual for the SmartAX MT882
ADSL Router
[here](http://dl.dropbox.com/u/5973603/SmartAX%20MT882%20ADSL%20Router.exe)
(the link might go dead unexpectedly, since it is served out of
Dropbox). This is a standard modem provided by Romtelecom (the Romanian
telecom provider) and I couldn’t find it elsewhere because Huawei is
very secretive about its stuff (the files were copied from the CD
provided with the modem). The driver makes the USB connection work as a
network card (which is very elegant and simple).
