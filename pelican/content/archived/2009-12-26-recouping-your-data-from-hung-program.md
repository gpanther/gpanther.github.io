Title: Recouping your data from a hung program
Date: 2009-12-26 21:15
Author: Attila-Mihaly Balazs
Slug: recouping-your-data-from-hung-program
Status: published

Scenario: you are typing away in your blog editor on Ubuntu doing a
(somewhat) Flash-heavy post. You make the mistake of hitting "Preview"
and the blogging software hangs. How can you get your post out?

1.  Find the PID of your blogging software
2.  Coredump it (`gcore [PID]` - this will create a file called
    `core.[PID]` in the current directory) - sidenote: interestingly,
    coredumping doesn't actually kill the application - this makes me
    wonder about thread safety... What guarantees does gcore make about
    the consistency of the dumped state? Probably none... This isn't
    important in this case, since the program is hung for good.
3.  Use a hex editor ([GHex](http://live.gnome.org/Ghex) for example)
    and search for a part of the blogpost. You will probably find it
    multiple times, but you can easily identify one occurrence which has
    a complete copy.
4.  Copy the blogpost from the hexeditor
5.  Profit!

Hope this saves somebody from retyping their text!

PS. This can be applied to other programs too where the storage format
is "human readable" (like text editors - as opposed to spreadsheet
editors). An other trick you might try is to search for the string as
Unicode (since more international-aware programs might store it as
that). While GHex doesn't support this directly, you can manually insert
the 00 bytes between the Latin characters. An other option would be to
run strings on the coredump file with different `--encoding` options.
