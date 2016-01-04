Title: Microbenchmarking and you
Date: 2011-03-07 15:13
Author: Attila-Mihaly Balazs
Tags: benchmark, java
Slug: microbenchmarking-and-you
Status: published

*Crossposted from the [Transylvania JUG
website](http://www.transylvania-jug.org/archives/174).*

Microbenchmarking is the practice of measuring the performance
characteristics (like CPU, memory or I/O) of a small piece of code to
determine which would be better suited for a particular scenario. If I
could offer but one advice on this, it would be this: don't. It is too
easy to get it wrong and bad advice resulting from bad measurement is
like cancer.

If you don't want to take my first advice, here is my second advice: if
you really want to do microbenchmarking watch this talk by Joshua Bloch:
[Performance Anxiety](http://parleys.com/#sl=3&st=5&id=2103) and use a
framework like [caliper](http://code.google.com/p/caliper/), which I
present below.

[caliper](http://code.google.com/p/caliper/) is a Java framework written
at Google for doing Java microbenchmarks as correctly as possible. To
use, first you have to build it (there are no prebuild jars yet, nor is
it present in the central Maven repository, sorry):

    svn checkout http://caliper.googlecode.com/svn/trunk/ caliper
    cd caliper
    ant

Now you can start writing your benchmark. Benchmarks are written in a
style similar to the JUnit3 tests:

-   you have to extend the `com.google.caliper.SimpleBenchmark` class
-   your methods must conform to the `public void timeZZZZ(int reps)`
    signature
-   you can override the setUp and tearDown methods to implement
    initialization / finalization

Below is a simple example (taken from the caliper homepage):

    public class MyBenchmark extends SimpleBenchmark {
      public void timeMyOperation(int reps) {
        for (int i = 0; i < reps; i++) {
          MyClass.myOperation();
        }
      }
    }

To run this you have multiple possibilities:

-   Use the `caliper` script included in the code distribution (this is
    a SH script, so it won't work under Windows):

        ~/projects-personal/caliper/build/caliper-0.0/caliper --trials 10 org.transylvania.jug.espresso.shots.d20110306.MyBenchmark

    <p>
    you can also execute the script without parameters to get a list and
    description of command line parameters.

-   Run it from your favorite IDE. You need to add the following
    libraries: allocation.jar, caliper-0.0.jar. The main class is
    com.google.caliper.Runner and the parameters are the same you would
    pass to the caliper runner
-   Add a main method to your test class which would contain the
    following:

        public static void main(String... args) throws Exception {
          Runner.main(MyBenchmark.class, args);
        }

By default caliper outputs an easy to understand text output. You have
also the option to publish the benchmark as a nice HTML page (see [this
page](http://microbenchmarks.appspot.com/run/jessewilson@google.com/examples.ArraySortBenchmark)
for example). The publication is done trough a Google AppEngine app and
is publicly available to anyone (a caveat to remember). For more
information see the [caliper questions on
StackOveflow](http://stackoverflow.com/questions/tagged/caliper). You
might also be interested in the [java performance tunning
website](http://www.javaperformancetuning.com/) if you need to perform
such tasks.
