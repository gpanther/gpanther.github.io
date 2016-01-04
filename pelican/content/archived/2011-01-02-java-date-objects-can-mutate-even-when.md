Title: Java Date objects can mutate, even when read
Date: 2011-01-02 10:43
Author: Attila-Mihaly Balazs
Tags: programming, multithreading, java
Slug: java-date-objects-can-mutate-even-when
Status: published

Ran into this problem a couple of months ago, when we saw some strange
dates in production. So I dug into the Java library sources (thank you
Sun for providing those!) and found that Date objects aren't always
"normalized". Rather, sometimes a "denormalized" value is stored which
is later (lazily) normalized. The normalized value isn't properly
synchronized with regards to the Java memory model however, which means
that sometimes you can get weir (and incorrect!) results.

To illustrate the problem, I've created [a small
program](http://code.google.com/p/hype-free/source/browse/trunk/java-data-mutation/DataMutation.java).
It does the following:

1.  It creates a Date object and sets it to certain values
2.  Schedules multiple Runnable's which examine the value of the object
    on a threadpool

Everything looks fine and dandy, right? The object isn't changed
(apparently) after being handed of to the threadpool, yet sometimes
wrong answers still appear (it takes around \~30 min on my laptop for
such an event). So what are the lessons here?

-   Get your API right! If the user doesn't *seem* to be doing writing,
    don't do writing!
-   You can still do lazy initialization (if you really want to), but be
    sure to make it thread-correct (volatile, synchronized, etc) or at
    least document it (even though nobody reads the documentation)
-   Source code FTW! I couldn't have debugged this without source code.
    Ok, maybe I could (decompiling class files is not that hard), but
    probably I wouldn't have bothered.
-   Finally, the solution (hack) in this particular situation is to call
    `getTime()` after setting the values, which preemptively normalizes
    the internal representation. Of course the proper solution would be
    to pass around truly immutable objects (like timestamps or value
    objects from [Joda Time](http://joda-time.sourceforge.net/)).

