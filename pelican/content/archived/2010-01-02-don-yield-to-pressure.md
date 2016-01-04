Title: Don't Yield to pressure?
Date: 2010-01-02 20:21
Author: Attila-Mihaly Balazs
Tags: programming, multithreading, profiler, java
Slug: don-yield-to-pressure
Status: published

or: does Thread.yield have its place in todays Java programs?

I was profiling a rather old legacy codebase (since the first rule of
performance optimization is "profile it" with the close second of "have
clear goals in mind" - but that's an other post) and - after optimizing
the first few hotspots,
[Thread.yield](http://java.sun.com/javase/6/docs/api/java/lang/Thread.html#yield%28%29)
appeared at the top of the most timely methods. I was intrigued, since I
didn't use yield since I wrote "cooperative multitasking" programs for
Windows 3.1 in VB 3 (and I'm not [a big Python
programmer](http://docs.python.org/reference/simple_stmts.html#yield)
either). So I scoured the 'net for Information on why/when you should
use Thread.yield, but came up with relative few pieces of information:

-   I found indications that some old Linux kernels behaved poorly on
    single processor machines if Thread.yield wasn't used (as in: one
    thread consuming all the CPU)
-   There were discussion about using Thread.sleep(0) vs. Thread.yield
    (apparently there is a difference regarding the treatment of
    remaining time-quantum by the scheduler)
-   ... this was pretty much it ...

So I've decided to do some micro-benchmarks. They consisted of a
producer and a consumer thread, connected by an unbounded queue (a
LinkedBlockingQueue to be more exact) and I measure the number of items
produced / consumer in 10 seconds. The first set of measurements were
performed on a dual-core machine, while the second set in a VM to
simulate a single-CPU system (it's kind of ironic that one has to
perform simulation to evaluate single-core systems). This isn't meant to
be a performance, evaluation, thus all the numbers are normalized to the
produced/direct number.

<style>
#java_yield_results_table { width: 100%; }<br></br>
#java_yield_results_table th { text-align: left; }<br></br>
#java_yield_results_table td { text-align: right; }<br></br>
</style>
<table id="java_yield_results_table" border="1" cellpadding="0" cellspacing="0">
<tr>
<th>
</th>
<th colspan="2">
2 CPUs

</th>
<th colspan="2">
1 CPU

</th>
</tr>
<tr>
<th>
Direct

</th>
<td>
1

</td>
<td>
1

</td>
<td>
1

</td>
<td>
0.06

</td>
</tr>
<tr>
<th>
Thread.yield()

</th>
<td>
0.12

</td>
<td>
0.12

</td>
<td>
0.04

</td>
<td>
0.04

</td>
</tr>
<tr>
<th>
Thread.sleep(0)

</th>
<td>
0.1

</td>
<td>
0.1

</td>
<td>
0.04

</td>
<td>
0.04

</td>
</tr>
<tr>
<th>
Priority - 1

</th>
<td>
0.81

</td>
<td>
0.81

</td>
<td>
1

</td>
<td>
0.05

</td>
</tr>
</table>
(My) conclusions:

-   These days there is no need for "helping" the OS scheduler out. Both
    of the proposed methods (yield and sleep) reduced the throughput of
    the system considerably.
-   Speaking of throughput: make a decision about the (performance)
    numbers your system should achieve. This includes both throughput
    and delay. Concrete (and realistic!) numbers. "As good as possible"
    is not a number! Neither is "better than the current". Then profile
    and optimize it until the numbers are achieved and no further.
-   In the case of a single CPU system there was a big imbalance between
    the speed of the producer and consumer which Thread.yield (or
    Thread.sleep) seemed to solve. Consider however, that this
    "solution" comes at the price of (almost) two orders of magnitude
    reduction in the throughput. A much better solution would be (in
    case you are in the rare situation of single CPU - maybe you're on a
    VPS, or you have multiple CPUs, but the number of threads far
    outweigh the number of CPUs) to use a bounder queue. This way the
    producer gets slowed down (by blocking repeatedly) if it produces
    faster than the consumer can consume. Then again, you need consider
    if this is acceptable for your application. Maybe the "overflow"
    situation is rare and it is more important to handle each element
    (and there are enough resources for it in the long run) than
    response speed. You have to know your application and its
    priorities. There is no way around it.

Finally I would like to leave you with the following short (\~30 min)
presentation about performance optimization on the JVM: [Making every
millisecond count! JVM performance tuning in the
real-world](http://skillsmatter.com/podcast/cloud-grid/making-every-millisecond-count-jvm-performance-tuning-in-the-real-world).
