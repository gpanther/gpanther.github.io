Title: Processing clipboard data in Perl
Date: 2011-01-03 17:03
Author: Attila-Mihaly Balazs
Tags: ubuntu, perl
Slug: processing-clipboard-data-in-perl
Status: published

The problem: lets say you have a program which generates data to the
clipboard (or it is easier to get the data into the clipboard than into
a file) and you want to process the data (create a summary for example).

Perl to the rescue!

Get the
[Clipboard](http://search.cpan.org/~king/Clipboard-0.13/lib/Clipboard.pm)
module (if you use Linux, it is as easy as
`sudo cpan -i Clipboard; sudo apt-get install xclip` but the package is
also available as an ActivePerl package for example).

Write a script like the following:

    use strict;
    use warnings;
    use Clipboard;

    my $clippy = Clipboard->paste();
    my ($sum, $cnt) = (0, 0);
    while ($clippy =~ /Processed in: (\d+)/g) {
            $sum += $1;
            $cnt += 1;
    }

    print $sum/$cnt, "\n";

</code>

Profit!!! :-)

*Update*: you can combine this with [syntax
highlight](http://advent.rjbs.manxome.org/2010/2010-12-13.html) for
example to obtain nicely formatted source code.

*Update*: copying stuff to the clipboard doesn't seem to work under
Linux (tested under Ubuntu 10.10) because it invokes xclip with the
"primary" clipboard but it only seems to work with the "clipboard"
clipboard. Unfortunately I didn't find any good material about the
distinction between these different clipboard types, but the "monkey
patch" below fixes the problem for me (of course I also [filed a
bug](https://rt.cpan.org/Public/Bug/Display.html?id=65399) with the
package so this should be resolved in a future version).

    use strict;
    use warnings;
    use Clipboard;

    if ('Clipboard::Xclip' eq $Clipboard::driver) {
      no warnings 'redefine';
      *Clipboard::Xclip::all_selections = sub {  
        qw(clipboard primary buffer secondary)
      };
    }

    # ... your code here ...
    Clipboard->copy('foofooo1');
