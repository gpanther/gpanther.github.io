Title: Ensuring the order of execution for tasks
Date: 2012-12-21 21:13
Author: Attila-Mihaly Balazs
Tags: multithreading, java advent, java
Slug: ensuring-order-of-execution-for-tasks
Status: published

*This post was originally published as part of the [Java Advent
series](http://www.javaadvent.com/2012/12/ensuring-order-of-execution-for-tasks.html).
If you like it, please spread the word by sharing, tweeting, FB, G+ and
so on! Want to write for the Java Advent blog? We are looking for
contributors to fill all 24 slot and would love to have your
contribution! [Contact Attila Balazs](mailto:dify.ltd@gmail.com) to
contribute!*

Sometimes it is necessary to impose certain order on the tasks in a
threadpool. [Issue 206 of the JavaSpecialists
newsletter](http://www.javaspecialists.eu/archive/Issue206.html)
presents one such case: we have multiple connections from which we read
using NIO. We need to ensure that events from a given connection are
executed in-order but events between different connections can be freely
mixed.

I would like to present a similar but slightly different situation: we
have N clients. We would like to execute events from a given client in
the order they were submitted, but events from different clients can be
mixed freely. Also, from time to time, there are "rollup" tasks which
involve more than one client. Such tasks should block the tasks for all
involved clients (but not more!). Let's see a diagram of the situation:

<div class="separator" style="clear: both; text-align: center;">

![](http://1.bp.blogspot.com/-TuCHb25JBqM/UNOOV5-EjwI/AAAAAAAAFo4/KoIJZOXz2Y8/s320/Untitled%2Bdrawing%2B%25281%2529.png)

</div>

As you can see tasks from client A and client B are happily processed in
parallel until a "rollup" task comes along. At that point no more tasks
of type A or B can be processed but an unrelated task C can be executed
(provided that there are enough threads). The skeleton of such an
executor is available [in my
repository](http://code.google.com/p/hype-free/source/browse/trunk/java-grouped-threadpool/src/main/java/com/blogger/hypefree/GroupedThreadPool.java).
The centerpiece is the following interface:

    public interface OrderedTask extends Runnable {
        boolean isCompatible(OrderedTask that);
    }

Using this interface the threadpool decides if two tasks may be run in
parallel or not (A and B can be run in parallel if
`A.isCompatible(B) && B.isComaptible(A)`). These methods should be
implemented in a fast, non locking and time-invariant manner.

The algorithm behind this threadpool is as follows:

-   If the task to be added doesn't conflict with any existing tasks,
    add it to the thread with the fewest elements.
-   If it conflicts with elements from exactly one thread, schedule it
    to be executed on that thread (and implicitly *after* the
    conflicting elements which ensures that the order of submission is
    maintained)
-   If it conflicts with multiple threads, add tasks (shown with red
    below) on all but the first one of them on which a task on the first
    thread will wait, after which it will execute the original task.

<div class="separator" style="clear: both; text-align: center;">

![](http://4.bp.blogspot.com/-IcwKi0hwcyA/UNSsiYecUPI/AAAAAAAAFpU/zk41QVcuxLo/s320/Untitled%2Bdrawing%2B%25282%2529.png)

</div>

More information about the implementation:

-   The code is only a proof-of-concept, some more would would be needed
    to make it production quality (it needs code for exception handling
    in tasks, proper shutdown, etc)
-   For maximum performance it uses lock-free\* structures where
    available: each worker thread has an associated
    ConcurrentLinkedQueue. To achieve the sleep-until-work-is-available
    semantics, an additional Semaphore is used\*\*
-   To be able to compare a new OrderedTask with currently executing
    ones, a copy of their reference is kept. This list of copies is
    updated whenever new elements are enqueued (this is has the
    potential of memory leaks and if tasks are infrequent enough
    alternatives - like an additional timer for weak references - should
    be investigated)
-   Compared to the solution in the JavaSpecialists newsletter, this is
    more similar to a fixed thread pool executor, while the solution
    from the newsletter is similar to a cached thread pool executor.
-   This implementation is ideal if (a) the tasks are (mostly) short and
    (mostly) uniform and (b) there are few (one or two) threads
    submitting new tasks, since multiple submissions are mutually
    exclusive (but submission and execution isn't)
-   If immediately after a "rollup" is submitted (and before it can be
    executed) tasks of the same kind are submitted, they will
    unnecessarily be forced on one thread. We could add code rearrange
    tasks after the rollup task finished if this becomes an issue.

Have fun with [the source
code](http://code.google.com/p/hype-free/source/browse/trunk/java-grouped-threadpool/src/main/java/com/blogger/hypefree/GroupedThreadPool.java)!
(maybe some day I'll find the time to remove all the rough edges).

\* somewhat of a misnomer, since there are still locks, only at a
lower - CPU not OS - level, but this is the accepted terminology

\*\* - benchmarking indicated this to be the most performant solution.
This was inspired from the implementation of the ThreadPoolExecutor.

*Meta: this post is part of the [Java Advent
Calendar](http://javaadvent.com/) and is licensed under the [Creative
Commons 3.0 Attribution](https://creativecommons.org/licenses/by/3.0/)
license. If you like it, please spread the word by sharing, tweeting,
FB, G+ and so on! Want to write for the blog? We are looking for
contributors to fill all 24 slot and would love to have your
contribution! [Contact Attila Balazs](mailto:dify.ltd@gmail.com) to
contribute!*
