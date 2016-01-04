Title: What VirusTotal is not
Date: 2009-11-09 13:34
Author: Attila-Mihaly Balazs
Tags: av, rant
Slug: what-virustotal-is-not
Status: published

![2139429\_dedfc5706f\_b](http://lh4.ggpht.com/_hrvCBhtWhJ4/Svf-VEd4lrI/AAAAAAAACB8/A2MEjuzcJ64/2139429_dedfc5706f_b%5B2%5D.jpg?imgmax=800 "2139429_dedfc5706f_b")
Since its inception [VirusTotal](http://www.virustotal.com/) has been
used by people to compare different AV products (just in case you don’t
know: VirusTotal is great free service which scans the uploaded file
with 40 AV engines currently and reports back the results). The AV
industry has objected to this practice because of a couple of reasons,
some more valid than others IMHO.

Today however I want to talk about the practice of saying “(only) X% of
AV detect this” and then giving a VirusTotal link. Two recent examples:
[here](http://blog.mxlab.eu/2009/11/07/facebook-updated-account-agreement-email-contains-sasfis-trojan/)
and [here](http://securitylabs.websense.com/content/Alerts/3501.aspx)
(to be clear: I don’t have anything against the particular blogs /
companies / authors – there are many more examples of this practice,
these are just two recent ones which came to my attention).

Why is this percentage meaningless and serves only to perpetuate FUD?

-   As I first argument I could mention all the discussion about AV
    engine configuration (this is frequently raised in discussion
    regarding the detection discussion, so I won’t dissect it further).
    A very thoroughly discussed argument is also that VT results
    represent a “point in time” rather than “now” (ie. detections since
    the scanning might have changed).
-   The second argument would be: VirusTotal goes for quantity not
    necessarily quality. Ie. the fact that a given engine is included in
    the list of engines used by VirusTotal isn’t a statement about the
    engine resource use, detection rate or false positive rate. Again,
    this doesn’t mean that the engines used are of low quality, it just
    means that VirusTotal isn’t in the AV engine testing business. It
    doesn’t say anything about the market share of the product either.
-   This means that the affirmation “X% of the engines detect a given
    file on VT” isn’t equivalent with the affirmation “X% of the users
    using AV are protected” or “AV software is X% effective”. However
    these are the thoughts which appear (by association) in a readers
    mind when seeing the initial affirmation.
-   Furthermore, some engines appear in multiple products (for example
    [GData integrates
    BitDefender](http://www.bitdefender.com/site/view/strategic-relationships.html)
    – amongst others) while other engines appear “split” (for example
    the McAfee desktop product contains both the “classical” and “cloud”
    engine, however on VT they appear as two separate entries “McAfee”
    and “McAfee+Artemis” respectively). If these relations are not
    considered (and I’m almost sure that they aren’t – given that these
    relations are not always publicly documented and they can change
    over time), the results come out skewed.

Conclusion: please *never, ever* take the VT result page and copy-paste
the percentage from it! *Do* provide permalinks to the result pages and
you can even make some sensible general statements (like “most of the
major AV vendors detect this threat” or “this threat is not well
detected by the smaller, Asian AV companies, but given its reliance on
the English language for social engineering, it might not be such a big
threat”). However, giving percentage wreaks of FUD and smells of
negative propaganda (do we really want to be at each-others throat,
analyzing which vendor doesn’t detect what? – there would be no winners
in such a discussion). Lets concentrate on giving sensible security
advice to users instead.

Picture taken from [Peter Kaminski's
photostream](http://www.flickr.com/photos/peterkaminski/) with
permission.
