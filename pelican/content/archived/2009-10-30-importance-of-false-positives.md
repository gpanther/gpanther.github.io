Title: The importance of false positives
Date: 2009-10-30 16:11
Author: Attila-Mihaly Balazs
Tags: av, security, praise
Slug: importance-of-false-positives
Status: published

![2748438226\_c0ed3e06f6\_o](http://lh5.ggpht.com/_hrvCBhtWhJ4/Sur0Ic4lteI/AAAAAAAACBI/Edd5q7VWGiA/2748438226_c0ed3e06f6_o%5B2%5D.jpg?imgmax=800 "2748438226_c0ed3e06f6_o")
An interesting paper was bought to my attention recently by [this blog
post](http://foregroundsecurity.com/index.php?option=com_content&view=article&id=114:the-second-false-positive&catid=42&Itemid=195):
[The Base Rate Fallacy and its implications for the difficulty of
Intrusion
Detection](http://www.raid-symposium.org/raid99/PAPERS/Axelsson.pdf).
The central question of this paper is: if we have a flow of N packets
per day and our network IDS has a false-positive rate of X, what is the
probability that we are experiencing a real attack, given that the IDS
says that we are? The paper uses Bayes’ theorem (of which you can find
[a nice explanation
here](http://oscarbonilla.com/2009/05/visualizing-bayes-theorem/)) to
put some numbers in and to get horrifying results (*many* false alerts),
and to conclude that such a rate of FPs seriously undermines the
credibility of the system.

The issue of false positives is also a concern in the anti-malware
industry. And while I
[rant](http://hype-free.blogspot.com/search/label/rant) quite a bit
about the AV industry, you have to give this one to them: the number of
false positives is *really* low. For example, in the
[AV-Comparatives](http://www.av-comparatives.org/) test 20 false
positives is considered many~~, even though the collection is over 1 500
000 samples (so the acceptable FP rate is below 0.0015%!)~~. *Update*:
David Harley was kind enough to correct me, because I was comparing
apples (the number of *malware* samples) to oranges (the number of
*clean* files falsely detected). So here is an updated calculation: the
Bit9 Global File Registry has more than 6 billion files indexed (they
index clean files). Consider whatever percent from that which is used by
AV-Comparatives for FP testing (as David correctly pointed out, the
cleanset size of AV-Comparatives is not public information – although I
would be surprised if it was less than 1 TB). Some back-of-the-napkin
calculations: lets say that AV-Comparatives has only one tenth of one
percent of the 6 billion files, which would result in 600 000 files.
Even so, 20 files out of 600 000 is just 0.003%.

Now there were (and will be) a couple of big f\*\*\*-ups by different
companies (like detecting files from Windows), but still, consumers have
a very good reason to trust them. Compare this with more “chatty”
solutions like [software
firewalls](http://hype-free.blogspot.com/2006/09/software-vs-hardware-firewalls.html)
or – why not – the UAC. Any good *security* solution needs to have at
least this level of FPs and much better detection. AV companies with low
FP rates – we salute you!

</p>
<p>
<center>
http://www.youtube-nocookie.com/v/xMUgmU\_Hsjc&hl=en&fs=1&color1=0x234900&color2=0x4e9e00\#t=1ms50

</center>
</p>
PS. There might be an argument to be made that different false-positives
should be weighted differently (for example depending on the popularity
of the file) to emphasize the big problems (when out-of-control
heuristics start detecting Windows components for example). That is a
valid argument which can be analyzed, but the fact remains that FP rates
of AV solutions, is very low!

Picture taken from [wadem's
photostream](http://www.flickr.com/photos/wadem/) with permission.
