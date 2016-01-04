Title: In praise of Regexp::Assemble
Date: 2010-03-15 10:42
Author: Attila-Mihaly Balazs
Tags: regex, programming, perl
Slug: in-praise-of-regexpassemble
Status: published

...and of the Perl modules in general. I had the following problem:

> Given a list of 16 character alphanumeric IDs, find all the lines from
> a large-ish (\~6GB) logfile which contain at least one of the IDs.

The naive approach was to construct a big regular expression like
`\W(\QID1\E|\QID2\E|\QID3\E...)\W` and match it against every line (I
needed to capture the actual ID to know in which bucket to place the
line). Needless to say, as it is the case with most naive approaches, it
was slooooow (basically, it was hogging the CPU, not the disk). So, by
searching around a little bit I found
[Regexp::Optimizer](http://search.cpan.org/~dankogai/Regexp-Optimizer-0.15/lib/Regexp/Optimizer.pm)
and
[Regexp::Assemble](http://search.cpan.org/dist/Regexp-Assemble/Assemble.pm).
Of the two the later seemed the more mature one, so – after quickly
installing it with CPAN – I’ve put it into my code and made it run at
the “speed of the disk”. W00t! Perl + CPAN + clever modules rock!

PS. A little benchmark data (take it with a grain of salt, since you
should be [profiling not
benchmarking](http://blog.urth.org/2010/03/benchmarking-versus-profiling.html)
most of the time):

-   Unoptimized regex size: 873 427 characters
-   Optimized regex: 69 536 characters
-   Unoptimized regex matchtime over 380 MB of data: \~1.9 hours (which
    would mean a throughput of \~58KB / sec – well below disk speed)
-   Optimized regex matching over the same 380 MB of data: 2 sec
    (throughput: 190 MB/sec !!!)

How cool is this?
