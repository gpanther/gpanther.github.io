Title: Recording test performance with Jenkins
Date: 2011-09-20 19:16
Author: Attila-Mihaly Balazs
Tags: jmeter, jenkins, maven, java, jug
Slug: recording-test-performance-with-jenkins
Status: published

In many (most?) systems performance is an important non-functional
requirement. And even if you attained the required performance, it is
useful to keep an eye on it to detect if a codechange involuntarily
deteriorates it. Enter the [Performance
plugin](https://wiki.jenkins-ci.org/display/JENKINS/Performance+Plugin)
for [Jenkins](http://jenkins-ci.org/). Using it you can record the
performance (as in: speed of execution) of your test runs and set alter
thresholds which cause the build to fail. Also it can generate graphs
like the one below:

![](http://www.transylvania-jug.org/wp-content/uploads/2011/09/respondingTimeGraph.png)

To do this:

-   Have Jenkins installed
-   Intstall the Performance plugin (or upgrade to the latest version,
    since there was [a
    bug](https://issues.jenkins-ci.org/browse/JENKINS-9655) in earlier
    versions which prevented the parsing of the JUnit reports)
-   For your build check “Publish Performance test result report” and
    add locations where the reports should be collected from.
-   That’s it! Future builds will collect the performance data and you
    can access it using the “Performance Trend” link (at the job level)
    or the “Performance Report” link (at the build level)

More details / caveats:

-   The paths are defined as ANT file expressions (that is you can use
    “\*\*” to specify an arbitrary level of directories, for example:
    `target/surefire-reports/**/TEST*.xml`)
-   JUnit performance is grouped at the test-class level, thus it
    probably makes sense create separate project / module which group
    the performance test cases.
-   [Benchmarking is hard](http://www.transylvania-jug.org/archives/174)
    and JUnit doesn’t give you any provisions to do warmup or to repeat
    the tests multiple times. To make your test as relevant as possible
    you should do this manually (warmup code can be placed in the
    @Before method for example). A properly set up JMeter task accounts
    for this already.
-   TestNG tests can also be parsed as long as the test run is set to
    produce a JUnit compatible report.
-   Slightly off-topic: to integrate a JMeter run into your maven build,
    you can use the
    [AntRun](http://maven.apache.org/plugins/maven-antrun-plugin/)plugin:` `



        maven-antrun-plugin
        1.6


        test







        run




Article originally posted to the [Transylvania JUG
blog](http://www.transylvania-jug.org/archives/241).
