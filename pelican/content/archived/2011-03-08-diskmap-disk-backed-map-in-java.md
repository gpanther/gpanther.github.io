Title: DiskMap - an disk backed Map in Java
Date: 2011-03-08 18:12
Author: Attila-Mihaly Balazs
Tags: java
Slug: diskmap-disk-backed-map-in-java
Status: published

I have the following problem: a Java application was running out of
memory. It was not feasible to mandate 64 bit JVM for this application
and the \~1.4G limit wasn't enough.

My solution was to implement a Map which - when an element is added -
also saves the value to disk and only holds a weak reference to the
value. When the memory pressure occurs, these objects, only linked by
the weak references are evicted. Later, when they need to be read, they
are read from the backing file.

Limitations:

-   Adding elements takes considerably longer (because they need to be
    serialized)
-   There is no way to reclaim space from the backing file (this is only
    intended for short-running mostly read-only tasks)
-   This is only useful if the values are considerably larger than the
    keys (because the keys are kept in-memory and only the values have
    the potential to be removed)
-   There is a memory overhead: when the objects are in-memory, you will
    take up an additional 20 to 40 bytes per entry. However, when the GC
    kicks in will only take up a 20 to 40 bytes per key.

Long story short: you can find the code (together with unit-tests) [in
my
repo](http://code.google.com/p/hype-free/source/browse/#svn%2Ftrunk%2Fjava-diskmap).
