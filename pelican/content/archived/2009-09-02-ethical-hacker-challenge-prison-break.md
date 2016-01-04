Title: Ethical Hacker challenge “Prison Break” solution
Date: 2009-09-02 15:44
Author: Attila-Mihaly Balazs
Tags: challenge, solution
Slug: ethical-hacker-challenge-prison-break
Status: published

As I usually do, I’ll publish my entry for the [Ethical Hacker
challenge](http://hype-free.blogspot.com/2009/07/new-ethical-hacker-challenge.html)
after the deadline passed:

*Challenge Question 1*: What is the most probable reason Michael could
not get network connectivity from the desk Ethernet jack?  What actions
should the team take to determine exactly what is going on, collect full
traffic captures, and gain full access to the network?

Most probably the switch to which the given port is connected has MAC
address filtering turned on. To circumvent this, they must clone the MAC
address of the VOIP phone.

The easiest way to do this is to start capturing the traffic on the
network interface of the laptop and then plug the VOIP phone into it.
The initial packets (most probably DHCP requests) will reveal the phone
MAC address. Sidenote: most ethernet ports these days are auto-sensing
(ie. no crossover cable is required). But just to make sure, one should
use a crossover cable or an intermediate switch (not hub!) is one is
available. After the MAC address has been determined, the host OS should
be instructed to use the given MAC address for the laptop network card.
You can find instructions for Linux here:
<http://linuxhelp.blogspot.com/2005/09/how-to-change-mac-address-of-your.html>
and for Windows here:
<http://www.irongeek.com/i.php?page=security/changemac>

Sidenote: given that the packet captures show two distinct networks
(192.168.1.0/24 and 172.29.0.0/16), it is clear that the administrators
have tried to separate the computer networks from the VOIP one. However,
relying only on different (sub-)nets is extremely weak and at least VLAN
level separation should have been implemented (then again, maybe the
available switches don't have VLAN features). 172.29.0.0/16 most
probably is the VOIP network, since we see SIP packets on it and
192.168.1.0/24 the computer network.

If only MAC filtering is implemented, after changing the MAC address, it
is possible to join any of the two available networks, meaning that they
can interact with the "computer" network, even if the given port was
originally assigned to a VOIP phone.

*Challenge Question 2*: What tool should Lincoln download, if any, to be
able to capture traffic on the desktop computer?

Sectools.org contains a nice list of available packet sniffers (
<http://sectools.org/sniffers.html> ). Given the constraints, my tool of
choice would be WinDump, the Windows port of tcpdump (
<http://www.winpcap.org/windump/install/> )

*Challenge Question 3*: Starting with the reverse connection from the
desktop computer, describe a step-by-step approach that could be applied
prior to 09:00 the next day in order to capture the network traffic on
the remote network and get a capture file for further in-depth analysis.
Make sure your approach follows Michael's advice to avoid detection.

-   download WinDump (
    <http://www.winpcap.org/windump/install/bin/windump_3_9_5/WinDump.exe>
    ) and WinPcap to the laptop
-   use the instructions provided at the following link to construct a
    portable version of WinPcap:
    <http://paperlined.org/apps/wireshark/winpcap_silent_install.html>
-   you can package up all the files (WinDump and the WinPcap DLLs +
    driver) into a single file using the SFX functionality from 7zip. To
    make sure that you don't get under the 0.5 meg limit, use Zip with
    the Store algorithm
-   upload the resulting file to the general's desktop (this part of the
    challenge is a little forced IMHO, since the IDS should have
    detected the reverse connection if it is sensible to long-lived, low
    traffic connections...)
-   launch the SFX, wait until all the files are extracted and copy
    npf.sys into c:\\Windows\\System32\\drivers
-   before 9:00 AM (at 8:55 for example) launch WinDump (this will
    capture at most 5 MB of data):

        WinDump -i 1 -w capture.pcap -C 5

-   after WinDump has stopped, retrieve the capture file and clean up
    (delete the driver, the SFX file, etc)

*Challenge Question 4*: Help the team complete this aspect of their
mission by analyzing the packet capture file collected on the desktop
computer and provide detailed information about the environment. Your
response should at least include the type of network traffic collected,
details about the General’s laptop computer, details about the Scylla
Codes server plus any other server available, and provide the names and
contents of the files stored on the server the input passphrase is based
on.

The collected traffic consists of 6 requests made to the Scylla server
(10.10.20.94) using HTTPS. To decode them, first convert the provided
key file into PEM format with OpenSSL:

</p>
    openssl rsa -in server.key -out server_key.pem 

Then use the resulting PEM file as described here for example to let
Wireshark decode the traffic:
<http://www.novell.com/coolsolutions/appnote/19321.html>

Now you can use the "Follow SSL stream" functionality from Wireshark to
analyze each request. From the headers it seems that the general's
laptop is running Windows Vista Media Center (tablet? edition), while
the Scylla server is running Linux/Apache:

</p>
    User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506) 
    Server: Apache/2.2.8 (Unix) mod_ssl/2.2.8 OpenSSL/0.9.8g DAV/2 PHP/5.2.9 

</p>
*Challenge Question 5*: What are the validation code and input
passphrase used by the General to generate the Scylla validation code
for this week?

The validation code is "6189db841f01413a05a53b7135137a17"

*BONUS QUESTION*: Briefly describe your recommendations about how The
Company could have detected and defended against the tactics you
described in your answer to Question 3.

The attack could have been prevented by using a whitelisting product
which doesn't let unknown executables be started. Other mitigating
measures would be:

-   using Group Policy to disable autorun
-   using Group Policy to controls what kind of USB devices can be used:
    <http://www.windowsecurity.com/articles/Control-USB-Devices-Group-Policy.html>
-   using a switched network
-   using an outbound proxy and make sure that only valid HTTP/HTTPS
    traffic can leave the network

One could work around many of these restrictions (for example: finding a
vulnerability in an installed software, running meterpreter in-process,
killing the whitelisting software, masking the outbound connection as a
HTTP one, using ARP spoofing to get around the switched network, etc),
but it raises the bar considerably.
