Title: Back with a vengeance
Date: 2009-09-29 12:22
Author: Attila-Mihaly Balazs
Tags: security, encryption
Slug: back-with-vengeance
Status: published

I’ve had limited connectivity / time in the last couple of weeks, but
I’m back baby!

The lesson of the day: you shouldn’t let your AV vendor provide general
security. The lesson comes to us via [Graham Cluley’s Sophos
blog](http://www.sophos.com/blogs/gc/g/2009/09/24/guest-blog-sophos-free-encryption/),
which informs us that [Sophos released a free encryption
tool](http://www.sophos.com/products/free-tools/sophos-free-encryption.html).
So, what’s wrong with it?

-   It uses symmetric crypto! Let me repeat that for you: it uses
    symmetric cryptography and recommends that you communicate the
    encryption password to the counterparty via an other communication
    channel. So much for ease of use and the asynchronous nature of
    email!
-   The feature sheet starts out by declaring that PKI has failed us,
    and then it touts a proprietary centralized solution for managing
    passwords.

In conclusion: this is a software which shouldn’t have been made. It is
simplistic, cumbersome to use and provides no added benefit over using
something like [7-zip](http://www.7-zip.org/) with encryption (which
also uses AES, also does compression – most probably better compression
– and it to can create SFX password protected archives).

Go and install Thunderbird with
[Enigmail](http://enigmail.mozdev.org/home/index.php).

For added fun: the brochure says “Protects against “brute force” attacks
by increasing response times each time the user enters the wrong
password”, and they then proceed to give you a CLI and COM interface to
the program which can be used directly to bruteforce the archives and
without these timeouts. Nice!
