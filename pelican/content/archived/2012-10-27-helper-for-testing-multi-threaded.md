Title: Helper for testing multi-threaded programs in Java
Date: 2012-10-27 22:48
Author: Attila-Mihaly Balazs
Tags: multithreading, java, jug
Slug: helper-for-testing-multi-threaded
Status: published

This post was originally published on the [Transylvania
JUG](http://www.transylvania-jug.org/archives/5442) blog.

Testing multi-threaded code is hard. The main problem is that you  
invoke your assertions either too soon (and they fail for no good  
reason) or too late (in which case the test runs for a long time,  
frustrating you). A possible solution is to declare an interface like  
the following:

    interface ActivityWatcher {
     void before();
     void after(); 
     void await(long time, TimeUnit timeUnit) throws InterruptedException, TimeoutException;
    }

It is intended to be used as follows:

-   “before” is called before the asynchronous task is delegated to an  
    execution mechanism (threadpool, fork-join framework, etc) and it  
    increments an internal counter.
-   “after is called after the asynchronous task has completed and it
    decrements the counter.
-   “await” waits for the counter to become zero

The net result is that when the counter is zero, all your asynchronous
tasks have executed and you can run your assertions. See [the example
code](https://code.google.com/p/hype-free/source/browse/trunk/espresso-shots/src/org/transylvania/jug/espresso/shots/d20121009/TestMultithreading.java).
A couple more considerations:

-   There should be a single ActivityWatcher per test (injected trough
    constructors or a dependency injection framework)
-   In production code you will use a [dummy/noop
    implementation](https://code.google.com/p/hype-free/source/browse/trunk/espresso-shots/src/org/transylvania/jug/espresso/shots/d20121009/NoopActivityWatcher.java)
    which removes any overhead.
-   This only works for situations where the asynchronous are kicked of  
    immediately. Ie. it doesn’t work for situations where we have  
    periodically executing tasks (like every 5 seconds) and we would
    want to  
    wait for the 7th tasks to be executed for example.

One thing the above code doesn’t do is collecting exceptions: if the  
exceptions happen on different threads than the one executing the  
testrunner, they will just die and the testrunner will happily report  
that the tests passs. You can work around this in two ways:

-   use the [default
    UncaughtExceptionHandler](http://docs.oracle.com/javase/7/docs/api/java/lang/Thread.html#setDefaultUncaughtExceptionHandler%28java.lang.Thread.UncaughtExceptionHandler%29)  
    to capture all exceptions and rethrow them in the testrunner if
    they  
    arrise (not so nice because it introduces global state – you can’t
    have  
    two such tests running in parallel for example)
-   Extend activity watcher and code calling activity watcher such that
    it has a “`collect(Throwable)`” method which gets called with the
    uncaught exceptions and “`await`” rethrows them.

Implementing this is left as an exercise to the reader
:-).![;-)](http://www.transylvania-jug.org/wp-includes/images/smilies/icon_wink.gif)
