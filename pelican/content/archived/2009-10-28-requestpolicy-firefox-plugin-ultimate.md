Title: RequestPolicy Firefox Plugin – the ultimate NoScript
Date: 2009-10-28 16:54
Author: Attila-Mihaly Balazs
Tags: Firefox, review
Slug: requestpolicy-firefox-plugin-ultimate
Status: published

![3236129283\_d61fb9c429\_b](http://lh6.ggpht.com/_hrvCBhtWhJ4/SuhbIAORvuI/AAAAAAAACA0/eKd6dhJTVMM/3236129283_d61fb9c429_b%5B10%5D.jpg?imgmax=800 "3236129283_d61fb9c429_b")
I recently found out about the following Firefox plugin/addon:
[RequestPolicy](http://www.requestpolicy.com/) (via [this
blogpost](http://skeptikal.org/2009/10/browser-security-tools-requestpolicy.html))
– see also [the Firefox addon
page](https://addons.mozilla.org/en-US/firefox/addon/9727/). Its
function is to whitelist *all* kinds of cross-domain requests, including
scripts, style-sheets, images, objects (Flash, Java, Silverlight), etc.
Anything in a webpage hosted on the domain A can reference other content
from domain A, but if it references content from other domains, it must
be present in the RequestPolicy whitelist. There are three types on
entries which can be added to the whitelist:

-   source (ie. pages on domain S can reference anything)
-   destination (ie. anything can reference domain D)
-   source-to-destination (ie. pages on domain S can reference resources
    on domain D)

There are still [some
glitches](https://www.requestpolicy.com/dev/ticket/50) to work out, but
all in all it is a good tool for the security conscious. So is it worth
it? It depends. If you are not a power-user who has some knowledge HTML
(ie. how CSS, HTML, JS and plugin objects fit together to form the
page), I would recommend against it (because you will have the
experience of webpages “not working for no good reason”). It takes some
initial training (just like NoScript), but after that it is pretty
invisible (even though not as invisible as NoScript, because it blocks
images / style-sheets).

![RequestPolicy](http://lh4.ggpht.com/_hrvCBhtWhJ4/SuhbIjA14OI/AAAAAAAACA4/kKlBjIl9ZCE/RequestPolicy%5B7%5D.png?imgmax=800 "RequestPolicy")

Does it make you more secure? Yes, but just in the “[you don’t have to
outrun the bear](http://www.aarons-jokes.com/joke-8002.shtml)”: once the
attacker has enough control to insert a linked resource (script, iframe,
etc) in a page, s/he almost certainly has enough control to insert the
attack script directly in the page, rather than linking to it. The
current practice of linking to a centralized place is mostly because the
attackers want to have centralized control (for example to add new
exploits) and statistics. Would such a whitelisting solution to become
widely used, they could switch with very little effort to the “insert
everything into the page” model. Still, such a solution shouldn’t be
underestimated, since it gives an almost perfect protection under the
current conditions.

*Update*: If leaving digital trails is something you like to avoid, take
into consideration that the fact that a given site is present in the
whitelist of addons such as NoScript or RequestPolicy can be considered
proof that you've visited the given site (unless it is on the default
list of the respective addon). Just something to consider from a privacy
standpoint. Life is a series of compromises and everyone has to decide
for herself how to make them.

Picture taken from [Luke Hoagland's
photostream](http://www.flickr.com/photos/lukehoagland/) with
permission.
