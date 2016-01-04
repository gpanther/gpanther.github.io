Title: Forensic analysis of JPEG images
Date: 2010-01-11 18:07
Author: Attila-Mihaly Balazs
Tags: security, forensics, images
Slug: forensic-analysis-of-jpeg-images
Status: published

![384044012\_e88180a76c\_o](http://lh3.ggpht.com/_hrvCBhtWhJ4/S0tM0IrXR1I/AAAAAAAACGU/i4PAk5AqZD8/384044012_e88180a76c_o%5B2%5D.jpg?imgmax=800 "384044012_e88180a76c_o")
Recently I became aware of the [Hackerfactor
blog](http://www.hackerfactor.com/blog/), especially [the
posts](http://www.hackerfactor.com/blog/index.php?/archives/322-Body-By-Victoria.html)
[related
to](http://www.hackerfactor.com/blog/index.php?/archives/346-Body-of-Answers.html)
[discovering](http://www.hackerfactor.com/blog/index.php?/archives/297-Blurring-The-Truth.html)
[image
manipulation](http://www.hackerfactor.com/blog/index.php?/archives/112-Error-Level-Analyzer.html).
It is interesting to read what one can deduce from an image, even when
one doesn’t use such “obvious” information sources like image metadata
(I say “obvious” because it seems that it isn’t obvious at all for most
people – but at least it can sanitized automatically). So here are the
links to the tools he recommends:

-   [Error Level
    Analyser](http://www.tinyappz.com/wiki/Error_Level_Analyser)
-   [ELC - Error Level Compare](http://www.socosoftware.com/ELC.htm)
-   [ELA From Scratch](http://infohost.nmt.edu/~schlake/ela/)

You might also find [this
paper](http://www.hackerfactor.com/papers/bh-usa-07-krawetz-wp.pdf)
interesting.

All in all, the most interesting thing for me was the fact *professional
image manipulators* (ok, I just made that word up, meaning “people who
know keyboard shortcuts in Photoshop”) repeatedly re-save the same image
in lossy formats like JPEG, thus compounding the loss of quality. Then
again, one should never underestimate human stupidity.

Picture taken from [Elsie esq.'s
photostream](http://www.flickr.com/photos/elsie/) with permission.
