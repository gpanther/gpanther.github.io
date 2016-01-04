Title: Should I use RoboForm?
Date: 2010-01-25 13:58
Author: Attila-Mihaly Balazs
Slug: should-i-use-roboform
Status: published

A little background about this post: while I was vaguely aware of
RoboForm, I never took a closer look at it until I saw the following
post by Derek: [Beware of fake shopping
sites](http://hijack-this.co.uk/2009/11/beware-of-fake-shopping-sites/).
What it basically says is that a password manager (such as Roboform)
will help you avoid phising sites, because it will observe the different
URL and will not pre-fill your contact details, thus providing you with
an additional warning sign that something is phishy :-)

I have a great deal of respect for Derek so I did some quick checking
around the product. Here are my findings:

-   My first question was: how does the company behind Roboform make
    money? Because if they don't have a clear way of making money and
    they are giving away the product for free, you might start to
    wonder - aren't they giving away my information to make money? I was
    relieved to find that they have a pro version which costs money.
    This doesn't necessarily mean that they *aren't* giving away your
    information, but there is one less reasons for them to do so.
-   The animated banner ad reminded me of some "smiley toolbar"
    advertisements which lead to adware, but taste is relative :-). An
    other marketing method of them which I personally found distasteful
    (although it is certainly legal) is the "[Free Password
    Scan](http://www.roboform.com/password-scanner.html)". This is a
    small tool which, when executed, shows the saved passwords from IE
    and Firefox. The purpose of this - I assume - is to show how
    "insecure" those browsers are (BTW, if you need such a tool, I would
    point you towards [the NirSoft
    utilities](http://www.nirsoft.net/password_recovery_tools.html)). I
    dislike FUD and negative campaigning (sadly it works quite well).
-   A quick test in a VM showed it working as advertised. I have one
    remark though: while it doesn't store the master password in memory
    (as the setup boldly points out), it *stores the individual account
    passwords in clear-text when it is unlocked*. You can check this out
    using something like [Process
    Hacker](http://processhacker.sourceforge.net/) or [Process
    Explorer](http://technet.microsoft.com/en-us/sysinternals/bb896653.aspx).
    You should point them to the actual browser process, since it is
    there where the passwords are stored, rather than the main RoboForm
    process.
-   One thing which Roboform *doesn't* do is to differentiate between
    the HTTP and HTTP**S** version of the sites. It happily fills the
    secure version of the page with credentials saved on the insecure
    version and vice-versa, potentially exposing the user to and
    [sslstrip](http://www.thoughtcrime.org/software/sslstrip/) type of
    an attack, which becomes more and more important because of the wide
    use of wireless technology.
-   Finally, I would like to comment on something Derek wrote in his
    post (so this *is not* an official statement from Roboform as far as
    I know): "ROBOFORM ... keeps all passwords in a secure encrypted
    database that only you (not a keylogger or malware) can access and
    use it". This is and isn't true. It is true that keyloggers won't
    see your individual passwords, but it will see your master password
    (!!!). Also, while Roboform will protect you against malware which
    specifically targets the password store of browsers (and there are
    quite a few of those out there), it *will not* protect you against
    the ones which inject themselves in the browser and simply capture
    the contents of any HTML forms which have an INPUT element of type
    PASSWORD in them - of course neither will SSL/TLS. And there are
    quite a few out there which do this.

In conclusion: I wouldn't trust my sensitive passwords to a closed
source program and I would always go with an open-source alternative.
Roboform isn't vastly superior in any particular way and the marketing
around it leaves a sour taste in my mouth.

BTW, the links on Derek's site are affiliate links - which is all nice
and good, I too have affiliate links in my blog postings occasionally -
but I would have liked a clear disclosure about this fact.
