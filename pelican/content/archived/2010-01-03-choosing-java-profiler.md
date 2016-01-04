Title: Choosing a Java profiler
Date: 2010-01-03 11:17
Author: Attila-Mihaly Balazs
Tags: programming, profiler, java
Slug: choosing-java-profiler
Status: published

Recently I've been looking around for a Java profiler (since the two
things you need for a successful performance tuning session are good
data and clear targets). I'll share the notes about my findings in the
hope that they might be useful for someone. Quick disclaimer: don't
believe everything you read on the Internet! These are my own findings /
experiences / opinions and they might not match yours. Also, they are
specific to this point in time. It is quite possible that later versions
of the given product fixes some / all of the problems I've experienced.
An other distinct possibility is that I've overlooked something. If this
is the case, please leave a comment and I'll update the post ASAP.

Options I've eliminated completely:

-   [AMD
    CodeSleuth](http://developer.amd.com/cpu/codeanalyst/codeanalystwindows/codesleuth/Pages/default.aspx) -
    even though it is free as in freedom (open source), it has some
    serious shortcomings: it needs Windows (!) + Java 1.6 (might be a
    problem if you're working with legacy apps) + Eclipse. Also, when
    I've tried to test it in a VM (VirtualBox running Windows XP on an
    Intel machine with VT-x enabled), it promptly bluescreend the
    machine (even though the documentation clearly says that you *do
    not* need an AMD processor to use it)
-   [JRat](http://jrat.sourceforge.net/)%20) - FLOSS, but it doesn't
    seem to be developed actively and has a limited set of features (but
    it worked, never skipping a beat, when I've tried it)
-   [Eclipse TPTP](http://www.eclipse.org/tptp/%20) (Test & Performance
    Tools Platform) - Eclipse specific. I've tried to install two
    different versions under Windows and - even though the installation
    seemed successful both times - it didn't function as expected (in
    fact, whenever I tried to launch an application in profile mode,
    Eclipse just hung)
-   [JProbe](http://www.quest.com/jprobe/) - Commercial, and it has a
    confusing licensing structure (I get easily confused - :-p)There are
    three components (Memory / Performance / Coverage Analysis) and each
    needs to be licensed separately...

I narrowed down my choices to three possibilities:

-   [YourKit from YourKit LLC](http://www.yourkit.com/)
-   [JProfiler from
    ej-technologies](http://www.ej-technologies.com/products/jprofiler/overview.html)
-   [the NetBeans profiler](http://profiler.netbeans.org/) (~~based on
    [VisualVM](https://visualvm.dev.java.net/)~~ - I have been informed
    that in fact the reverse is true: VisualVM reuses the profiling code
    from NetBeans)

Things they have in common:

-   Multi-OS support (Windows / Linux / Mac / Solaris)
-   Multi-IDE support (IntelliJ, Eclipse, Netbeans) - with the exception
    of the NetBeans profiler, obviously :-)
-   Support for multiple / older versions of Java (again, important if
    you are working on a legacy project): 1.4 / 1.5 / 1.6 0 with the
    exception of the NetBeans profiler, ~~which is based on VisualVM~~
    shares the profiling code with Visual VM, and - although I couldn't
    find any explicit mention about this in the NetBeans documentation,
    the VisualVM site has [a
    table](https://visualvm.dev.java.net/features.html#feature_matrix)
    which shows that profiling is not available for older versions of
    the JVM. *Update*: I have been informed (see the comment below) that
    these are not in fact limitations of the NetBeans IDE, only of
    VisualVM
-   Support for remote profiling (again, with the - possible - exception
    of NetBeans - the same situation as above)
-   Memory / CPU profiling
-   Thread state monitoring (runnable / running / blocked / waiting)
-   Dynamic instrumentation (no recompilation needed)
-   Saving and comparing of snapshots

CPU profiling overhead (measured by micro-benchmark which calculated PI
with increasing precision):

-   YourKit: \~5x slowdown
-   JProfiler: \~10x slowdown (remark: JProfiler has a nice feature
    which suggests methods to exclude after the first run - ie. methods
    from the base libraries which are very frequently called - to reduce
    the profiling overhead)
-   NetBeans / VisualVM: \~4x

Remarks: these were "full profiling" results. Some profilers (JProfiler
for example) support an alternative method: taking a look at the current
stack for each threat at each N ms. This alternative method has a much
smaller overhead and most of the time gives the same relative result
(ie. the ranking of the most costly methods) even if the absolute times
are not as accurate.

YourKit details:

-   <http://www.yourkit.com/purchase/index.jsp#licensing_policy>
-   It has the best integration with Eclipse from the three.
-   In the default setup it only shows the result after the application
    has (properly) ended. If the application terminates unexpectedly
    (for example you kill it), the results won't be shown
-   It has no wizards for running user-specified Java programs (ie. from
    outside of the IDEs)
-   I've been informed that both of the previous shortcomings can be
    avoided by using the "remote" profiling feature (ie. by starting
    your program manually with the given agent). While this very well be
    true, it also sounds extremely cumbersome.
-   A possible advantage is that they also have a .NET profiler in
    addition to the Java profiler, so if your programmers regularly work
    in "both worlds", or if you have distinct teams which do, you might
    be able to get a deal from them (I didn't see anything on their site
    indicating that there was such an offer, but I imagine that it can
    be negotiated)

JProfiler details:

-   <http://www.ej-technologies.com/buy/jprofiler/floating/volumeDiscounts?itemId=517127>
-   Has a simple wizard for starting applications
-   It was the only one from the three which could show the stacktrace
    for the threat *holding* the lock, not just for the one waiting for
    it (very important, since it removes a lot of the guesswork!)
-   It was the only one (out of the three) which threated locks from the
    java.util.concurrent.locks package the same as "synchronized" blocks
    (both in the thread view - where it correctly displayed "blocked"
    instead of "waiting" - and in the "monitor" view). The other
    profilers knew only about "synchronized"

NetBeans details:

-   FLOSS (Free, Libre, Open source software)
-   It has a decent profiler ~~with all the essential functionalities
    based on VisualVM~~ - see the comment below
-   ~~Unfortunately this means that it has the same limitations as the
    VisualVM technology: only local profiling on the 1.6 JVM is
    supported (this might or might not be a big deal for you)~~
-   I have been informed that NetBeans fully suppots older version of
    Java and also remote profiling scenarios.
-   One can use VisualVM directly, with the major advantage of being
    able to profile *any* local Java application in an ad-hoc manner
    (ie. the given application doesn't even have to be started with a
    specific java agent, it is injected dynamically). There are of
    course some limitations (as with any technology): AFAIK, there are
    some limitations to the "visibility" of local Java applications
    (something along the lines of "has to be started under the same
    account"). Also, I found situations where VisualVM was unable to
    successfully instrument an application (and I'm not really sure
    about the reasons). In such cases support for "pre-instrumentation"
    would be nice.
-   Also, [VisualVM 1.2 introduced the option to use a sampling
    profiler](http://blogs.sun.com/nbprofiler/entry/visualvm_1_2_released)
    for even lower overhead.

Personal conclusions:

-   JProfiler is the best money can buy (it seems that [I'm not alone
    with this
    opinion](http://skillsmatter.com/podcast/cloud-grid/making-every-millisecond-count-jvm-performance-tuning-in-the-real-world)),
    but it is very expensive (especially the "floating" licenses - they
    are really useful because they allow the product to be installed on
    an arbitrary number of machines, but only N of them can be used at
    the same time)
-   YourKit is mediocre (from the point of view of the capabilities),
    but it is considerably less expensive (especially the floating
    licenses)
-   NetBeans is nice, if you already use NetBeans or you can convince
    people to use NetBeans. In fact it is comparable with YourKit with
    regards to the feature set ~~with the two restrictions of local
    profiling on 1.6~~ and it is free! Alternatively, you can use
    VisualVM if you are at the start of your profiling journey (for
    example: you don't yet have the automated QA environment for
    performance regression testing).

HTH

PS. And remember: the two most important things for performance
optimization are: good data (collected by a profiler in an environment
which is as close to the production one as possible - there are a lot of
great profilers out there for many programming languages, for example
[Devel::NYTProof](http://blog.timbunce.org/2009/12/24/nytprof-v3-worth-the-wait/)
for Perl) and clear goals (along the lines of "lower the latency by 10%"
or "increase the throughput by 20%").
