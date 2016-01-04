Title: Carving out files with Perl
Date: 2010-01-26 16:11
Author: Attila-Mihaly Balazs
Tags: programming, perl, carving, file recovery
Slug: carving-out-files-with-perl
Status: published

I've had to use this trick a couple of times the last few years, so I
decided that I might as well document it:

If you have an image of a storage media (like an SD card or CD/DVD)
which you can not mount (either because the filesystem is hosed - that's
a technical term for damaged beyond repair :-) - or because it uses some
proprietary extension - \*cough\* MS \*cough) *and* you know the
approximate size of each file (maybe they are JPEGs or AVIs), you could
adapt [this script of
mine](http://code.google.com/p/hype-free/source/browse/trunk/carve.pl).

What it does:

1.  It reads `$search_buffer` bytes from `$input`
2.  It looks for `$header` (as it is written it looks for RIFF, which
    means AVI or WAV usually - for JPEG you would use "\\xFF\\xD8")
3.  If it finds it, it dumps `$extracted_size` bytes from the given
    position (this should be set to be larger than the biggest file you
    expect)
4.  It not, it seeks forward `$search_buffer - length($header)` (to
    handle the cases when the header is split by the border of the
    buffer)

The script is not perfect (for one it tries to load the entire file into
memory before writing it out; it also doesn't do any validation of the
fileformat, thus possibly creating some garbage output), but it worked
well for me in the past, so I thought I share it.

PS. If you need some more serious file recovery, you might want to look
at [PhotoRec](http://www.cgsecurity.org/wiki/PhotoRec) and
[TestDisk](http://www.cgsecurity.org/wiki/TestDisk). They are both free
(as in freedom - GPL license) and seem to be great programs (I never
actually managed to get them to recover more than my little cobbled
together script, but I might have some very particular usecases).
