Title: Is hand-writing assembly still necessary these days?
Date: 2011-02-06 09:14
Author: Attila-Mihaly Balazs
Tags: optimization, programming, javascript, assembly, c, performance, java
Slug: is-hand-writing-assembly-still
Status: published

[![12878535\_df4197ea6b\_o](http://lh6.ggpht.com/_hrvCBhtWhJ4/TU5KYLbHO1I/AAAAAAAADUo/XSFzXb1UgJ4/12878535_df4197ea6b_o_thumb%5B2%5D.jpg?imgmax=800 "12878535_df4197ea6b_o")](http://lh4.ggpht.com/_hrvCBhtWhJ4/TU5KXCBpA-I/AAAAAAAADUk/nz5JLoVBru8/s1600-h/12878535_df4197ea6b_o%5B4%5D.jpg)
Some time ago I came over the following article: [Fast CRC32 in
Assembly](http://wj32.wordpress.com/2010/09/19/fast-crc32-in-assembly/).
It claimed that the assembly implementation was faster than the one
implemented in C. Performance was always something I’m interested in, so
I repeated and extended the experiment.

Here are the numbers I got. This is on a Core 2 Duo T5500 @ 1.66 Ghz
processor. The numbers express Mbits/sec processed:

-   The assembly version from the blogpost (table taken from
    [here](http://www.koders.com/c/fid699AFE0A656F0022C9D6B9D1743E697B69CE5815.aspx?s=crc32#L19)):
    \~1700
-   Optimized C implementation (taken from the same source): \~1500. The
    compiler used was Microsoft Visual C++ Express 2010
-   Unoptimized C implementation (ie. Debug build): \~900
-   Java implementation using polynomials: \~100 (using JRE 1.6.0\_23)
-   Java implementation using table: **\~1900**
-   Built-in Java implementation: \~1700
-   Javascript (for the fun of it) implementation (using the code from
    [here](http://noteslog.com/post/crc32-for-javascript/) with
    optimization – storing the table as numeric rather than string) on
    Firefox 4.0 Beta 10: \~80
-   Javascript on Chrome 10.0.648.18: \~40
-   (No IE9 test – they don’t offer it for Windows XP)

Final thoughts:

-   Hand coding assembly **is not** necessary in 99.999% (then again 80%
    of all statistics are made up :-p). Using better tools or better
    algorithms (see the “Java table based” vs. “Java polynomial”) can
    give just as good of performance improvement. Maintainability and
    portability (almost always) trump performance
-   Be pragmatic. Are you sure that your performance is CPU bound? If
    you are calculating a CRC32 of disk files, a gigabit per second is
    more than enough
-   Revisit your assumptions periodically (especially if you are dealing
    with legacy code). The performance characteristics of modern systems
    (CPUs) differ enormously from the old ones. I would wager that on an
    old CPU with little cache the polynomial version would have
    performed much better, but now that we have CPU caches measured in
    MB rather than KB the table one performs much better
-   Javascript engines are getting better and better.

Some other interesting remarks:

-   The source code can be found [in my
    repo](http://code.google.com/p/hype-free/source/browse/#svn%2Ftrunk%2Fcrc32-benchmark).
    Unfortunately I can’t include the C version since I managed to
    delete it by mistake :-(
-   The file used to benchmark the different implementations was [a PDF
    copy](http://producingoss.com/en/producingoss.pdf) of the Producing
    Open Source Software book
-   The HTML5 implementation is surprisingly inconsistent between
    Firefox and Chrome, so I needed to add the following line to keep
    them both happy:
    `var blob = file.slice ? file.slice(start, len) : file;`
-   The Javascript code doesn’t work unless it is loaded via the http(s)
    protocol. Loading it from a local file gives “Error no. 4”, so I
    used a [small python
    webserver](http://hype-free.blogspot.com/2011/02/how-to-quickly-start-up-webserver-with.html)
-   Javascript timing has [some
    issues](http://ejohn.org/blog/accuracy-of-javascript-time/), but my
    task took longer than 15ms, so I got stable measurements
-   The original post mentions a variation of the algorithm which can
    take 16 bits at one (rather than 8) which could result in a speed
    improvement (and maybe it can be extended to 32 bits)
-   Be aware of the “free” tools from Microsoft! This article would have
    been published sooner if it wasn’t for the fact MSVC++ 2010 Express
    require an online registration and when I had time I had no Internet
    access!
-   *Update*: If you want to run the experiment with GCC, you might find
    the following post useful: [Intel syntax on
    GCC](http://xorl.wordpress.com/2009/01/01/intel-syntax-on-gcc/)

Picture taken from the [TheGiantVermin's
photostream](http://www.flickr.com/photos/tudor/12878535/) with
permission.
