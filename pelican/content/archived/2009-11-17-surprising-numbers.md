Title: Surprising numbers
Date: 2009-11-17 18:05
Author: Attila-Mihaly Balazs
Tags: security, FUD, probabilities
Slug: surprising-numbers
Status: published

![2801309954\_3af91bf56b\_o](http://lh5.ggpht.com/_hrvCBhtWhJ4/SwLJy7iPZgI/AAAAAAAACCM/AWEHSS94Wr8/2801309954_3af91bf56b_o%5B2%5D.jpg?imgmax=800 "2801309954_3af91bf56b_o")
I was reading the latest FudSec piece ([Generating a False Sense of
Insecurity](http://fudsec.com/generating-a-false-sense-of-insecurity))
where I found the following statement (emphasis added):

> Facebook now has 300 million users. Let’s assume that each user has at
> least one piece of user-generated content on their Facebook page
> cause, well, it’s a very user-content driven site. That means that of
> the 300 million home pages on Facebook that 95% (285 million) has
> either a malicious link or other insecure content. Conversely that
> means that 5% (15 million) are clean, uninfected, safe pages.
>
> The average Facebook user has 120 friends or 281 friends, depending on
> which news article you might be reading. Let’s just assume for
> mathematical purposes that the number is somewhere in the middle, at
> about 200 friends per user. Let’s pretend, too, that you visit every
> friend’s page in a single day. Because it’s your day off, of course,
> you wouldn’t actually do that at work.
>
> *The mathematical likelihood that one of your 200 friends is one of
> the 95% that is infected is infinitesimal.*

This statement seemed a little off. After all, we are selecting 200
pages out of 300 million where 275 million are infected. The chance to
get to an infected / malicious page can’t be that low, right? Wrong! The
problem as stated is known in mathematics (probability theory to be more
precise) as the “drawing without replacement” and apparently the
scientific name is [hypergeometric
distribution](http://en.wikipedia.org/wiki/Hypergeometric_distribution).
Long story short, Wikipedia pointed me to [a
calculator](http://pcarvalho.com/things/hypegeocalc/publish.htm) which
says that – given the parameters quoted above – you have a
99.9999608980365% chance that all of your friends will be clean /
non-malicious! Talk about counter-intuitive!

Conclusion? First of all, trust but verify. If you hear something which
sounds “off”, try to verify the information from multiple sources. Then
again, our brains don’t seem to be wired to evaluate probabilities
“heuristically”, so one should always sit down and work out the exact
math (there are a lot of free tools on the Internet which can help you)
before making important decisions.

Picture taken from [EraPhernalia Vintage's
photostream](http://www.flickr.com/photos/eraphernalia_vintage/) with
permission.
