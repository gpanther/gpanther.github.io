Title: Augmenting Log4J stack traces with class versions
Date: 2011-02-03 18:07
Author: Attila-Mihaly Balazs
Tags: log4j, stacktrace, java
Slug: augmenting-log4j-stack-traces-with
Status: published

If you have multiple versions of your code in production, it is
*extremely* useful for the log to include the version of the classes
when producing a stacktrace, otherwise it is very hard to match the
lines in the stacktrace with the lines of the source code (sidenote:
there is an optimization in the Sun JVM where - if an exception is
thrown "too much" - the JVM stops providing stacktrace - see [this
article](http://jawspeak.com/2010/05/26/hotspot-caused-exceptions-to-lose-their-stack-traces-in-production-and-the-fix/)
about it and to learn how to disable this feature).

If you are using Log4J as your logging framework, with a little magic
you can turn the following stacktrace:

    17:47:40,208 ERROR [main] [TestLog4jExtendedStacktrace] An exception has occurred!
    java.lang.IllegalArgumentException: Test exception
     at ...Callee.called(TestLog4jExtendedStacktrace.java:144)
     at ...Caller.call(TestLog4jExtendedStacktrace.java:136)
     ...

</code>

Into this (note the class versions at the bottom):

    java.lang.IllegalArgumentException: Test exception
     at ...Callee.called(TestLog4jExtendedStacktrace.java:144)
     at ...Caller.call(TestLog4jExtendedStacktrace.java:136)
     ...

    Callee: $Revision: 56 $
    Caller: $Revision: 56 $

</code>

The main mechanism is as follows:

-   Each class contains a static String field called "VCS\_VERSION".
    This field is set (trough the magic keyword substitution - see the
    documentation for
    [SVN](http://svnbook.red-bean.com/en/1.4/svn.advanced.props.special.keywords.html),
    [CVS](http://www-igm.univ-mlv.fr/~bedon/Enseignement/Outils/Docs/cvs/cvs_12.html))
    to the last version when the file was committed to your VCS.
-   When a stacktrace is sent to the logger, it will look at the classes
    and if they have the "VCS\_VERSION" field, it will output it at the
    end (it doesn't annotate the stacktrace itself, because some tools -
    like IDEs - depend on the stacktrace having a certain format for
    them to be able to process it - like adding one-click "go-to-line"
    shortcuts)

As usual, the source can be found [in the
repository](http://code.google.com/p/hype-free/source/browse/trunk/espresso-shots/src/org/transylvania/jug/espresso/shots/d20110203/TestLog4jExtendedStacktrace.java).

Some more implementation details: the current way of modifying the
stacktrace is quite hackish (adding a filter and trough reflection
modifying the passed in LoggingEvent object). However it has the
advantage of being usable without modifying your config files (ie. if
you have many config files, but can modify it in only one place in the
code, this is a good solution. More "proper" alternatives would be to
implement a "wrapper" appender (like
[AsyncAppender](http://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/AsyncAppender.html))
or a wrapper around
[Layout](http://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/Layout.html),
however both of these require you to modify your configuration files.
