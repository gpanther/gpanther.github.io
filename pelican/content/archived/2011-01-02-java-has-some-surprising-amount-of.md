Title: Java has some surprising amount of dinamism in it
Date: 2011-01-02 18:15
Author: Attila-Mihaly Balazs
Tags: programming, java
Slug: java-has-some-surprising-amount-of
Status: published

Not long ago I saw [some java code](http://pastie.org/1411379) from
[Simone Tripodi](http://people.apache.org/~simonetripodi/). It generates
synchronization wrappers around arbitrary objects at runtime in a
typesafe manner with a couple of easy to understand lines of code. The
heavy lifting is done by the dynamic proxy mechanism available from Java
1.5 if I recall correctly.

The downside is that there seems to be a 30% to 40% performance impact
based on some [quick
benchmark](http://code.google.com/p/hype-free/source/browse/trunk/java-dynproxy-perf/src/TestJavaDynproxyPerf.java)
I've done. However one can not understate the value of not having to
write or maintain code!

There are surprisingly many things one can do in Java in a typesafe
manner (including things usually associated with dynamic languages)
which helps catching more errors early (at compile time) and take full
advantage of the different helper features available in IDEs (such as
auto-complete).
