Title: One more thing…
Date: 2009-10-07 13:36
Author: Attila-Mihaly Balazs
Tags: rant, server, microsoft, web
Slug: one-more-thing
Status: published

[![214291449\_b0d7e78356\_b](http://lh6.ggpht.com/_hrvCBhtWhJ4/SsxvE1I-64I/AAAAAAAAB8w/dkg9DBXIdYU/214291449_b0d7e78356_b_thumb.jpg?imgmax=800 "214291449_b0d7e78356_b")](http://lh3.ggpht.com/_hrvCBhtWhJ4/SsxvETdNtFI/AAAAAAAAB8s/cWsnV2b0PLk/s1600-h/214291449_b0d7e78356_b%5B2%5D.jpg)
So, if I started ranting on Microsoft, here is one more thing: you
should *never ever* use Microsoft servers if you want to scale. The
reasons is simple: currently the best scaling method is horizontal (ie.
buy loads of cheap hardware and distribute the load between them). Using
Microsoft server software would mean that for each server you would need
to buy at least one license (or more, like in the case of MS Windows +
MS SQL Server). This can easily cost you almost as much (if not more)
than the hardware itself.

As far as I’m aware, only Microsoft and hosting providers (which recoup
the cost from their clients) are running MS servers in large numbers.
This is sustained by a quick check of the top \~5000 sites (as defined
by [Alexa](http://www.alexa.com/topsites)) – less than 16% of them run
IIS. To paraphrase Eminem:

> Be smart, don’t be a retard! You take advice from someone who run
> their front-end webserver tier on VM’s, even though *it makes no sense
> from a technology standpoint to do so*?

PS. Yeah, there is the BizPark program from MS for startups – but we yet
have to see the first large-scale success emerge from it (BTW, one of my
favorite site – StackOverflow – runs Windows Server trough the BizPark
program – and even they now use a Linux VM!).

Picture taken from [mark sebastian's
photostream](http://www.flickr.com/photos/markjsebastian/) with
permission.
