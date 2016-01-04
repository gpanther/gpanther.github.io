Title: Changes to String.substring in Java 7
Date: 2012-12-12 10:37
Author: Attila-Mihaly Balazs
Tags: java7, string, java advent, java
Slug: changes-to-stringsubstring-in-java-7
Status: published

*This post was originally published as part of the [Java Advent
series](http://www.javaadvent.com/2012/12/changes-to-stringsubstring-in-java-7.html).
If you like it, please spread the word by sharing, tweeting, FB, G+ and
so on! Want to write for the Java Advent blog? We are looking for
contributors to fill all 24 slot and would love to have your
contribution! [Contact Attila Balazs](mailto:dify.ltd@gmail.com) to
contribute!*

It is common knowledge that Java optimizes the substring operation for
the case where you generate a lot of substrings of the same source
string. It does this by using the `(value, offset, count)` way of
storing the information. See an example below:

<div class="separator" style="text-align: center">

![](http://4.bp.blogspot.com/-gnaLPXGMeUQ/UMIaKhQ5wsI/AAAAAAAAFn8/wNPgGPtE2qY/s320/Untitled%2Bdrawing.png)

</div>

In the above diagram you see the strings "Hello" and "World!" derived
from "Hello World!" and the way they are represented in the heap: there
is one character array containing "Hello World!" and two references to
it. This method of storage is advantageous in some cases, for example
for a compiler which tokenizes source files. In other instances it may
lead you to an OutOfMemorError (if you are routinely reading long
strings and only keeping a small part of it - but the above mechanism
prevents the GC from collecting the original String buffer). Some even
[call it a
bug](http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=4513622). I
wouldn't go so far, but it's certainly a leaky abstraction because you
were forced to do the following to ensure that a copy was made:
`new String(str.substring(5, 6))`.

<div class="separator" style="text-align: center">

![](http://3.bp.blogspot.com/-NGSJS_psCIc/UMW40g0NLXI/AAAAAAAAFoQ/7kfOVA8JdC0/s320/Untitled%2Bdrawing.png)

</div>

This all changed in [May of
2012](http://mail.openjdk.java.net/pipermail/core-libs-dev/2012-May/010257.html)
or Java 7u6. The pendulum is swung back and now full copies are made by
default. What does this mean for you?

-   For most probably it is just a nice piece of Java trivia
-   If you are writing parsers and such, you can not rely any more on
    the implicit caching provided by String. You will need to implement
    a similar mechanism based on buffering and a custom implementation
    of CharSequence
-   If you were doing `new String(str.substring)` to force a copy of the
    character buffer, you can stop as soon as you update to the latest
    Java 7 (and you need to do that quite soon since [Java 6 is being
    EOLd as we
    speak](https://blogs.oracle.com/java/entry/end_of_public_updates_for)).

Thankfully the development of Java is an open process and such
information is at the fingertips of everyone!

A couple of more references (since we don't say pointers in Java :-))
related to Strings:

-   If you are storing the same string over and over again (maybe you're
    parsing messages from a socket for example), you should [read up on
    alternatives to
    String.intern()](http://hype-free.blogspot.ro/2010/03/stringintern-there-are-better-ways.html)
    (and also consider reading chapter 50 from the second edition of
    Effective Java: Avoid strings where other types are more
    appropriate)
-   Look into (and do benchmarks before using them!) options like
    UseCompressedStrings (which [seems to have been
    removed](http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=7129417)),
    UseStringCache and StringCache

Hope I didn't strung you along too much and you found this useful! Until
next time  
- Attila Balazs

*Meta: this post is part of the [Java Advent  
Calendar](http://javaadvent.com/) and is licensed under the [Creative
Commons 3.0 Attribution](https://creativecommons.org/licenses/by/3.0/)
license. If you like it, please spread the word by sharing, tweeting,
FB, G+ and so on! Want to write for the blog? We are looking for
contributors to fill all 24 slot and would love to have your
contribution! [Contact Attila Balazs](mailto:dify.ltd@gmail.com) to
contribute!*
