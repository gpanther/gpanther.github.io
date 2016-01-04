Title: String.intern() – there are better ways
Date: 2010-03-22 13:04
Author: Attila-Mihaly Balazs
Tags: programming, java
Slug: stringintern-there-are-better-ways
Status: published

![4349787041\_f31a40baf4\_o](http://lh4.ggpht.com/_hrvCBhtWhJ4/S6dOwBNgXlI/AAAAAAAACPI/FTPGYo1Pepk/4349787041_f31a40baf4_o%5B2%5D.jpg?imgmax=800 "4349787041_f31a40baf4_o")
I don’t want to write a “considered harmful” article (because [they are
harmful](http://meyerweb.com/eric/comment/chech.html)), but after
experimenting with different solutions I do have a strong opinion that
there almost no reason to use String.intern() in Java. But let us
proceed step-by-step.

First of all, what does String.intern() do? Go read the
[Javadoc](http://java.sun.com/javase/6/docs/api/java/lang/String.html#intern%28%29)
for it and also take a look at [String
interning](http://en.wikipedia.org/wiki/String_interning) of Wikipedia.
The essence of it is that if you have two strings `s1` and `s2` such
that `s1.equals(s2)`, there will be only one copy of the string stored
if they are interned. From this definition follow the two usecases for
string interning:

1.  You read a lot of repetitive strings from an external source (a flat
    file or DB for example) and you need to keep them all in memory. In
    this case interning the strings has the potential to save you a lot
    of memory.
2.  You’ve determined (by [profiling your
    application](http://hype-free.blogspot.com/2009/07/profile-first.html)!)
    that `String.equals` is a hotspot for your application and you would
    like to replace those calls with the `==` operator.

If you have different reasons for looking at String.intern(), you should
think twice about them before going down the route. If you’ve thought
about long and hard, and you still think that String.intern is the best
solution for you, but not for any reason mentioned above, please leave
me a comment! (Also, read the rest of this post, since it might give you
a better alternative).

So, having the above usecases in mind, what is the problem with calling
String.intern?

1.  It is quite CPU intensive. Calling `new String("foo").intern()` can
    be an order of magnitude (10x to 15x based on some of my
    measurements) slower than `new String("foo")`.
2.  You have to remember to do it everywhere. This isn’t so fatal if
    you’re just aiming for reduced memory consumption, but if you forget
    to call “intern” somewhere and later use the “==” operator for
    comparing elements, you can create some hard to track down bugs.
3.  It can result in mysterious “OutOfMemory” exceptions. In the SUN JVM
    (which is the most widely used one) “internalized” String’s are
    stored in a special memory location called “PermGen”. The size of
    this isn’t influenced by the usual “-Xmx1024M” command line option,
    you have to remember (and to know about it in the first place!) to
    use the “-XX:MaxPermSize=512m” command line.

These are some very serious problems. What are the alternatives? The
easiest one is not to use String.intern. Ok, lets say that you’ve
*performed measurements* with *relevant, production data* and came to
the conclusions that your problems need to resolved using this method.
My recommendation would be the following:

-   Use a WeakHashMap to create a pool of Strings as describe [in this
    blog
    post](http://www.codeinstructions.com/2008/09/instance-pools-with-weakhashmap.html).
    This has the advantage that your cache won’t end up keeping the
    objects in memory after all the references to it have disappeared.
    Don’t forget to synchronize access to it if you’re planning on using
    it from multiple threads!
-   Always use String.equals, never “==”. If you take a peek at
    java.lang.String.equals, you will see that the first check that it
    does is “==”. By never using “==” explicitly you still will have
    most of the speed benefits, while eliminating the risk that you
    accidentally get a “rogue” String from somewhere and your code
    fails, even though the two strings are equal.

The advantages of the above solution are:

-   It is 30% to 50% faster than String.intern (although it is still
    slower than *not* calling String.intern. You should also watch out
    that it doesn’t become a chocking point in your application because
    of the synchronization if you are calling it from multiple threads).
-   It is safe (as mentioned above, forgetting to “make unique” some of
    the String’s doesn’t make your logic fail)
-   It doesn’t require special configuration on the JVM (like adjusting
    the PermGen size)

I will post some example code later this week when I’ll post the slides
for a presentation I’ll be giving to the local JUG, so be sure to keep
an eye on [my blog](http://hype-free.blogspot.com/) and [my code
repository](http://code.google.com/p/hype-free/source/browse/#svn/trunk).

Some resources on the topic:

-   [Busting java.lang.String.intern()
    Myths](http://www.codeinstructions.com/2009/01/busting-javalangstringintern-myths.html)
-   [interned Strings : Java
    Glossary](http://mindprod.com/jgloss/interned.html) (small trivia:
    substrings keep a reference to the original String, so if you’re
    keeping small parts of long String’s, you will be consuming much
    more memory than you might have anticipated)
-   [Is java.lang.String.intern() really
    evil?](http://kohlerm.blogspot.com/2009/01/is-javalangstringintern-really-evil.html)

Picture taken from [Mark Drago's
photostream](http://www.flickr.com/photos/markdrago/) with permission.
