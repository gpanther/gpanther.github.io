Title: RegEx which matches strings not containing a substring
Date: 2010-03-10 14:08
Author: Attila-Mihaly Balazs
Tags: regex
Slug: regex-which-matches-strings-not
Status: published

![2091640491\_33206332cb\_b](http://lh5.ggpht.com/_hrvCBhtWhJ4/S5eLoyAy4YI/AAAAAAAACOM/OaJ_SL080Gg/2091640491_33206332cb_b%5B2%5D.jpg?imgmax=800 "2091640491_33206332cb_b")
This is an interesting problem which can appear in certain cases
(although not very often). A little searching around led me to many
posts stating that there is no easy solution and [the following easy
solution](http://bloggernitin.blogspot.com/2007/12/regex-for-doesnt-contain.html):

> `^((?!my string).)*$`

It works as follows: the matching string must contain zero or more
characters which are *not preceded* (?! is the negative look behind
operator) by the given string.

It is quite straight-forward, uses operators which are widely supported
by regualar expression engines and works even if “my string” is at the
end of the string we are trying to match – for reasons which are not
entirely clear to me.

Obviously it is a hack and you shouldn’t use it if you can use a clearer
way to indicate your intention, but it is a nifty tool to have in your
toolbox for that one moment when you need it.

Picture taken from [crowt59's
photostream](http://www.flickr.com/photos/crowt59/) with permission.
