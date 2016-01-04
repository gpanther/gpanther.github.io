Title: Splitting hairs^H^H^H^H^H strings with Java
Date: 2010-01-24 21:55
Author: Attila-Mihaly Balazs
Tags: programming, java
Slug: splitting-hairshhhhh-strings-with-java
Status: published

<div style="float: right; padding: 3px;">

[![Split
Personality](http://farm3.static.flickr.com/2097/2225546021_4864c2bc72.jpg)](http://www.flickr.com/photos/nickwheeleroz/2225546021/ "Split Personality by nickwheeleroz, on Flickr")

</div>

Offtopic: where does \^H come from? (since I too found it only
recently) - from [the source of all
wisdom](http://en.wikipedia.org/wiki/Backspace) - Wikipedia :-p

> Pressing the backspace key on a computer terminal would generate the
> ASCII code 08, BS or Backspace, which would delete the preceding
> character. That control code could also be accessed by pressing
> Control-H, as H is the eighth letter of the Latin alphabet. Terminals
> which did not have the backspace code mapped to the function of moving
> the cursor backwards and deleting the preceding character would
> display the symbols \^H (caret, H — see Caret notation) when the
> backspace key was pressed. This sequence is still used humorously for
> epanorthosis by computer literates, denoting the deletion of a
> pretended blunder, much like overstriking.

Now back to our topic: how to split a String in Java into parts? Here
are a couple of options:

-   Use a
    [StringTokenizer](http://java.sun.com/javase/7/docs/api/java/util/StringTokenizer.html) -
    one thing which surprises Java novices is that the second parameter
    in the constructor *is a list of separators not one big separator*.
    So if you specify `", "`, this will split at *either commas or
    spaces, not at commas followed by spaces*.
-   Use
    [String.split](http://java.sun.com/javase/7/docs/api/java/lang/String.html#split%28java.lang.String%29) -
    this can also surprise novices since - even though it accepts a
    String parameter - the String will be compiled into regular
    expression (Pattern). While there are several warning signs (like
    the documentation - because everyone reads those :-p - or the
    parameter name), it is easy to ignore and one can get surprising
    results (like splitting the String `"aaa.bbb.ccc"` using the pattern
    `"."` and getting an empty String).
-   Precompiling a Pattern and using the
    [split](http://download.java.net/jdk7/docs/api/java/util/regex/Pattern.html#split%28java.lang.CharSequence%29)
    method on it. This has the advantage of expressing intent more
    clearly than the previous method and also being more efficient if
    one needs to split multiple strings using the same Pattern. However
    this still can be overkill if you just want to split using a single
    character (or even a list of characters).
-   Using the
    [StringUtils.split](http://commons.apache.org/lang/api/org/apache/commons/lang/StringUtils.html#split%28java.lang.String,%20char%29)
    method from the Apache Commons library (which *can* be used in
    commercial projects!) or even [roll your
    own](http://code.google.com/p/hype-free/source/browse/trunk/jsplit/JSplitTest.java).

When considering these alternatives you should consider expressiveness
first and performance second (also, don't optimize until a profiler
tells you to!). Luckily StringUtils is a clear choice from both points
of view, unless you need something more complex than one character
separators. Here are some performance numbers:

-   [Custom
    implementation](http://code.google.com/p/hype-free/source/browse/trunk/jsplit/JSplitTest.java)
    (Apache Commons should be in the same ballpark) - 1
-   StringTokenizer - 2.1
-   String.split - 3.46
-   Pattern.split - 2.87

These numbers shouldn't be taken as an absolute and they can depend on
many things (for example if a profiler is or isn't attached, the version
of the JVM, etc), but they should point you in the right direction.

*Update*: a very important note: while these solutions are mostly
drop-in replaceable, be aware that there are some differences between
them around the corner cases (ie. how they handle null's, what if the
string ends in a delimiter, what if two delimiters follow each other,
etc). If and when you decide to swap one for the other, be sure to
unittest your piece of code with the types of data you expect it to
handle.

So there you have it, more than you ever wanted to know about splitting
Strings :-) Hopefully this helps somebody.
