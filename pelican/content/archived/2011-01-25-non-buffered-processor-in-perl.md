Title: Non-buffered processor in Perl
Date: 2011-01-25 05:44
Author: Attila-Mihaly Balazs
Tags: perl
Slug: non-buffered-processor-in-perl
Status: published

Lets say that you have the following problem: you want to write a script
which processes the output of a program and writes out the modified
somewere, with as little buffering as possible. One concrete example
(for which I needed the script) is log rotation: you want to save the
output of a program (which doesn't support log rotation by itself) to a
logfile which gets rotate at midnight (because it includes the date in
the name). Also, an other constraint is that you would like to
“time-out” the read attempt to do some maintenance work (for example you
would like to rotate your logs – create the files with the different
dates - even when no data is written to it).

One possibility would have been to use
[IO::Select](http://perldoc.perl.org/IO/Select.html), however it doesn't
support filehandles on Windows (not that Windows wouldn’t have [the API
to do so](http://en.wikipedia.org/wiki/Overlapped_I/O), it’s just that
nobody was implemented it in Perl core). Fortunately we can have
something very similar to it:

    #!/usr/bin/perl
    use strict;
    use warnings;
    use IO::Handle;

    binmode STDIN;
    binmode STDOUT;
    STDIN->blocking(0);
    STDOUT->autoflush(1);

    my $BUFFLEN = 4096;
    while (1) {
      my $buffer;
      my $read_count = sysread(STDIN, $buffer, $BUFFLEN);
      
      if (not defined($read_count)) {
        # nothing to read, pause
        sleep 0.1;
        next;
      }
      if (0 == $read_count) {
        # EOF condition
        exit 0;
      }
      
      syswrite(STDOUT, $buffer);
    }

The magic is done here by `STDIN->blocking(0);` which sets the
filehandle into a non-blocking mode, returning “undef” is there is
nothing to read. Whenever this happens (ie. there is no data on the
input) it pauses for a brief moment (1/10 of a second) and then retries.

Some other remarks about the code:

-   the input is read and the output is written as binary. This means
    that no processing is done which could screw up the flow (for
    example trying to convert data between character sets and screwing
    up Unicode characters)
-   care is taken to introduce minimal buffering. Output is produced as
    soon as the input arrives. For more intricacies of Linux buffering
    see [this nice article at
    pixelbeat](http://www.pixelbeat.org/programming/stdio_buffering/).
-   the code is very performant. I’ve measured throughputs up to 1.4
    Gb/sec and can certainly handle anything the disk can (if we
    consider it in the context of log rotator)
-   the code has been tested and works on both Windows (Strawberry Perl
    5.12.1) and Linux. It should work mostly anywhere since it uses Core
    Perl.

