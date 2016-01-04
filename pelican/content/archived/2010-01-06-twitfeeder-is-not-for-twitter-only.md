Title: TwitFeeder is not for Twitter only
Date: 2010-01-06 11:37
Author: Attila-Mihaly Balazs
Tags: twitter, twitfeeder
Slug: twitfeeder-is-not-for-twitter-only
Status: published

The TwitFeeder has support for non-Twitter sources - crossposted from
[the TwitFeeder
blog](http://blog.thetwitfeeder.com/2010/01/twitfeeder-is-not-for-twitter-only.html):

> The TwitFeeder uses the Twitter API to get the different bits and
> pieces of information needed to generate the enhanced RSS feed.
> However Twitter isn’t the only one exposing the API:
>
> -   Laconi.ca (now [Status.Net](http://status.net/)) is an “Open
>     source microblogging service” and it exposes an API which is
>     almost 100% compatible with the Twitter API and you can see it in
>     action on Laconi.ca sites like [Identi.ca](http://identi.ca/) or
>     [The TWiT Army](http://army.twit.tv/) (the Status.Net wiki also
>     contains a [large list of
>     installs](http://status.net/wiki/ListOfServers))
> -   Wordpress.org [recently added support for a subset of the Twitter
>     API](http://en.blog.wordpress.com/2009/12/12/twitter-api/)
>
> What does this mean for users? All the Twitter specific tools just
> became more usable, leading to more integration and less time-wasting
> (which is the main idea behind this site). You can use the TwitFeeder
> to subscribe to any site which exposes the Twitter API:
>
> -   Subscribe to one of Identi.ca’s founder:
>     [identi.ca/evan](http://www.thetwitfeeder.com/html/identi.ca/evan)
> -   Subscribe to Leo Laporte on the Twit Army:
>     [army.twit.tv/leolaporte](http://www.thetwitfeeder.com/html/army.twit.tv/leolaporte)
> -   Subscribe to a Wordpress blog (most of the blogs already have an
>     RSS feed, but just for the fun of it):
>     [wordpress.com/decipherinfosys](http://www.thetwitfeeder.com/html/wordpress.com/decipherinfosys)
>
> More API support = Less siloed information = More fun
>
> Programmers sidenote: there is no “official” compatibility test for
> the API, so you can never be sure that you are perfectly compatible –
> there will be always some gray areas (for example the exact link to a
> status message – which varies between different implementations). All
> you can do is to have rigorous unit tests. And code reuse either using
> [our sources](http://code.google.com/p/twitfeeder/) or
> [pything-twitter](http://code.google.com/p/python-twitter) to which
> we’ve [contributed support for multiple
> sources](http://code.google.com/p/python-twitter/issues/detail?id=114).
