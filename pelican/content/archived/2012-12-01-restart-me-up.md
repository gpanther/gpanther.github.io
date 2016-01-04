Title: (Re)Start me up!
Date: 2012-12-01 18:24
Author: Attila-Mihaly Balazs
Tags: fork, daemon, launch, process, java advent, java
Slug: restart-me-up
Status: published

*This post was originally published as part of the [Java Advent
series](http://www.javaadvent.com/2012/12/restart-me-up.html).*

There are cases where you would like to start a Java process identical
to the current one (or at least using the the same JVM with tweaked
parameters). Some concrete cases where this would be useful:

-   Auto-tuning the maximum memory parameters (ie. you have an algorithm
    to determine the optimal value - for example: 80% of the system
    memory - and your JVM wasn't started with that particular value)
-   Creating a cluster of processes for high(er)-availability (true HA
    implies multiple physical nodes) or because processes have different
    roles (like the components in MongoDB).
-   Daemonizing the current process (that is, the background process
    should run even after the launching process has terminated) - this
    is a very frequent modus-operandi for programs on \*nix systems
    where you have the foreground "control" process and the background
    "daemon" process (not to be confused with the "daemon" threads).

Doing this is relatively simple - and can be done in pure Java - after
you find the correct API calls:

``` {style="overflow: auto;"}
List arguments = new ArrayList();
// the java executable
arguments
  .add(String.format("%s%sbin%sjava",
    System.getProperty("java.home"), File.separator,
    File.separator));
// pre-execuable arguments (like -D, -agent, etc)
arguments.addAll(ManagementFactory.getRuntimeMXBean()
  .getInputArguments());

String classPath = System.getProperty("java.class.path"), javaExecutable = System
  .getProperty("sun.java.command");
if (classPath.equals(javaExecutable)) {
 // was started with -jar
 arguments.add("-jar");
 arguments.add(javaExecutable);
} else {
 arguments.add("-classpath");
 arguments.add(classPath);
 arguments.add(javaExecutable);
}

// we might add additional arguments here which will be received by the
// launched program
// in its args[] paramater
arguments.add("runme");

// launch it!
new ProcessBuilder().command(arguments).start();
```

</code>

Some explanations about to the code:

-   It is largely inspired from [this
    project](https://github.com/brianm/gressil)
-   We suppose that the java executable is named `java` and is located
    in `bin/java` relative to `java.home`. We use `File.separator` for
    the code to be portable.
-   [getInputArguments](http://docs.oracle.com/javase/7/docs/api/java/lang/management/RuntimeMXBean.html#getInputArguments%28%29)
    is used to get specific arguments passed to the JVM (like `-Xmx`).
    It does **not** include the classpath.
-   Which is taken from `java.class.path`
-   Finally, there is one heuristic step: we try to detect if we were
    launched using the `-jar myjar.jar` syntax or the `MyMainClass`
    syntax and replicate it.

This is it! After that we use
[ProcessBuilder](http://docs.oracle.com/javase/7/docs/api/java/lang/ProcessBuilder.html)
(which we should always favour over Runtime.exec because it auto-escapes
the parts of the command line for us).

A final thought: if you intend to use this method to "daemonize" a
process (that is: to ensure that it stays running after its parent
process has terminated) you should do two things:

-   Redirect the standard input and output. By default they are
    redirected into temporary buffers and the JVM will seemingly
    randomly terminate when those buffers (pipes) fill up.
-   Under Windows use `javaw` instead of `java`. This ensures that the
    process won't be tied to the console it was started from (however it
    will still be tied to the user login session and will terminate when
    the user logs out - for a more heavy-duty solution look into the
    [Java Service
    Wrapper](http://wrapper.tanukisoftware.com/doc/english/download.jsp)).

This is it for today, hope you enjoyed it, fond it useful. If you run
the code and it doesn't work as advertised, let me know so that I can
update it (I'm especially interested if it works with non Sun/Oracle
JVMs). Come back tomorrow for an other article!

*Meta: this post is part of the [Java Advent
Calendar](http://javaadvent.com/) and is licensed under the [Creative
Commons 3.0 Attribution](https://creativecommons.org/licenses/by/3.0/)
license.*
