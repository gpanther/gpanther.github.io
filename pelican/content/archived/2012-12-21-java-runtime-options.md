Title: Java Runtime options
Date: 2012-12-21 21:06
Author: Attila-Mihaly Balazs
Tags: command line, java advent, java
Slug: java-runtime-options
Status: published

*This post was originally published as part of the [Java Advent
series](http://www.javaadvent.com/2012/12/java-runtime-options.html). If
you like it, please spread the word by sharing, tweeting, FB, G+ and so
on! Want to write for the Java Advent blog? We are looking for
contributors to fill all 24 slot and would love to have your
contribution! [Contact Attila Balazs](mailto:dify.ltd@gmail.com) to
contribute!*

The Java runtime is a complex beast - and it has to be since it runs
officially on seven platforms and unofficially on many more. Give this,
it is normal that there are many knobs and dials to control how things
function. The more well known ones are:

-   -Xmx for the maximum heap size
-   -client and -server for selecting the default set of parameters from
    classes of defaults
-   -XX:MaxPermGen for controlling the permanent generation size

Other than these, it is (very) rarely the case that you need to change
the defaults. However, thanks to Java being open source you can see the
list of options, their default values and a short explanation directly
[from the source
code](http://hg.openjdk.java.net/jdk7/jdk7/hotspot/file/b92c45f2bc75/src/share/vm/runtime/globals.hpp).
Currently there are almost 800 options in there!

An other way to see the options (but one which doesn't display the
explanations unfortunately) is the following command:

    java -XX:+UnlockDiagnosticVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+PrintFlagsFinal -version

These options are well worth studying. Not for tweaking them (since
there is a wealth of testing behind the defaults the extent of which
would be very hard to replicate), but rather to understand the different
functionalities offered by the JVM (for example [why you might not see
stacktraces in
exceptions](http://hype-free.blogspot.com/2009/07/why-cant-i-see-stacktrace-under-java.html)).

*Meta: this post is part of the [Java Advent
Calendar](http://javaadvent.com/) and is licensed under the [Creative
Commons 3.0 Attribution](https://creativecommons.org/licenses/by/3.0/)
license. If you like it, please spread the word by sharing, tweeting,
FB, G+ and so on! Want to write for the blog? We are looking for
contributors to fill all 24 slot and would love to have your
contribution! [Contact Attila Balazs](mailto:dify.ltd@gmail.com) to
contribute!*
