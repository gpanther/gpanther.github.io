Title: A (mostly) cross-platform clickable map of Romanian counties
Date: 2012-11-01 10:06
Author: Attila-Mihaly Balazs
Slug: a-mostly-cross-platform-clickable-map
Status: published

<div class="separator" style="clear: both; text-align: center;">

[![](http://2.bp.blogspot.com/-efBtXhgduhw/UJItSwviTnI/AAAAAAAAFjw/-D_TsgQlsUs/s320/Screenshot%2Bfrom%2B2012-11-01%2B10%253A02%253A31.png)](http://hype-free.googlecode.com/svn/trunk/map-romania/index.html)

</div>

TL;DR - I've created a map of Romania's counties (judete) using
Javascript which can be used as an alternative for drop-down boxes
during form input. It works great with FF and Chrome :-). See it [in
action](http://hype-free.googlecode.com/svn/trunk/map-romania/index.html)
and browse [the source
code](http://code.google.com/p/hype-free/source/browse/#svn%2Ftrunk%2Fmap-romania).

The map is based on [the SVG drawings from Wikimedia
Commons](https://commons.wikimedia.org/wiki/Atlas_of_Romania)
postprocessed in Inkscape to simplify the paths (and to remove the Black
Sea from it). After that it was converted to
[Raphael.js](http://raphaeljs.com/) using
[readysetraphael](http://readysetraphael.com/). I also use
[ScaleRaphael](http://www.shapevent.com/scaleraphael/) to be able to
render it at an arbitrary size. According to
[BrowserStack](http://www.browserstack.com/) (a great service well worth
its money BTW if you do web development!) it works with Firefox
(starting with version 3.6), Chrome and Safari. IE has a hard time with
it, but hopefully as the underlying library improves, it will start to
work :-).
