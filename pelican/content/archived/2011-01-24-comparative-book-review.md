Title: Comparative book review
Date: 2011-01-24 17:42
Author: Attila-Mihaly Balazs
Tags: review, book, concurrency, java
Slug: comparative-book-review
Status: published

Below is a a short comparative review of tow books about Java
concurrency which I've read in the last couple of months. Disclaier: the
Amazon links are affiliate ones.

[![](http://3.bp.blogspot.com/_hrvCBhtWhJ4/TT2c4haJJWI/AAAAAAAADTg/ShRRPEb9EHk/s200/51AG8p4X7WL._SL160_.jpg)](http://www.amazon.com/gp/product/0321349601?ie=UTF8&tag=hypefree-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0321349601)

Java Concurrency in Practice is an interesting book, which should be a
must-read for anyone doing concurrent programming in Java (and in these
days if you aren’t, you’re missing out on a whole lot of possible
performance improvement). While some reader criticize it for the dense
stile, it is hard to see how one could tackle such a complicated topic
in simpler way (to paraphrase Albert Einstein: one needs to make things
as simple as they need to be and no simpler). That said, the book
definitely has the topics ordered from simple to more advanced, so even
if you find the idea of reading the whole book daunting, you should look
at the first couple of chapters at least. I would especially recommend
chapter 3 (Sharing Objects) from part I (Fundementals) which should give
a clear motive to everyone why they should be concerned by thread-safety
and how they should reason about concurrent programs (I find that many
concurrency errors occur because people have a naive and simplistic
understanding of the way concurrency works on modern hardware).

[![](http://2.bp.blogspot.com/_hrvCBhtWhJ4/TT2diMcyd-I/AAAAAAAADTo/PcrXEzkm9aY/s200/51F057WGQNL._SL160_.jpg)](http://www.amazon.com/gp/product/0201310090?ie=UTF8&tag=hypefree-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0201310090)

Concurrent Programming in Java: Design Principles and Pattern (2nd
Edition): The CPiJ book is much older, ancient even by computer age
standards (published in 1999, compared to the JCiP book published in
2006). If also describes a much more manual, tedious way of doing things
compared to the newer book. Also, it talks about the precursor of the
java.util.concurrent package, since the package didn’t exists back then.
All in all: if possible, get the JCiP book. If you already have the CPiJ
book, it is a good introduction to the topic, however be ware that much
of the advice is outdated and Java 6 (and even Java 5) contain better
and simpler ways to perform the tasks described in the book.
