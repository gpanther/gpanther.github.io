Title: The leaked Microsoft COFEE product
Date: 2009-11-09 14:09
Author: Attila-Mihaly Balazs
Tags: forensics, microsoft
Slug: leaked-microsoft-cofee-product
Status: published

![176571915\_de1226bb5d\_b](http://lh4.ggpht.com/_hrvCBhtWhJ4/SvgGe3EUOPI/AAAAAAAACCE/TI_dnPcCqMA/176571915_de1226bb5d_b%5B2%5D.jpg?imgmax=800 "176571915_de1226bb5d_b")
So, the Microsoft COFEE (Computer Online Forensic Evidence Extractor)
tool was leaked. I took a quick look at it, and – as expected – there is
nothing “magical”, “secret” or “backdoorish” about it (even though I
*love* the picture which comes with [the Gizmodo
article](http://gizmodo.com/5399377/microsoft-cofee-some-of-the-most-illegal-software-you-can-pirate),
the text itself is complete and utter BS – COFEE isn’t a tool “that
helps law enforcement grab data from password protected or encrypted
sources” as the article claims).

So what *is* Microsoft COFEE?

-   it is a collection of information gathering tools which are either
    built into Windows (ie. net, arp, ipconfig) or can be freely
    downloaded from the Microsoft website (ie. pslist)
-   it contains a simple case-management software which helps users
    prepare a USB stick that need to be inserted in the target computer
    and manage the collected information
-   the software on the USB stick is executed either using the autorun
    mechanism or by manually launching it. *There is no built-in
    functionality to bypass passwords or other protection mechanisms*
-   It also contains a detailed analysis of the registry / filesystem
    fingerprint of each tool (this is important if the other party
    argues that running the tool caused modifications on the system
    which are pertinent to the case)

Conclusion: there is no magical pixie dust here, move along! (in fact,
it is quite similar with the [winenum Metasploit
script](http://metasploit.com/svn/framework3/trunk/scripts/meterpreter/winenum.rb)).

*PS/Update*: regarding the "defense" against these tools: first of all,
they all seem to be user-mode tools. This means that they probably have
limited capability of detecting kernel-mode rootkits. Also - from what
I've seen - they are all public tools, so there is a good chance that
there exists malware out there there which "defends" itself against
these software. Again, no magic.

Now before you conclude that this is utterly useless - if I were a IT
forensicator :-p, I would prefer having this data compared to no data at
all. It will give you some basic idea of the system (or the network for
that matter if ran on every PC) which may enable you to come back with a
very precise target in mind.

Picture taken from [raddaqii's
photostream](http://www.flickr.com/photos/raddaqii/) with permission.
