Title: How slow is Java reflection?
Date: 2016-08-08 18:31
Author: Attila-Mihaly Balazs
Tags: java, benchmark, reflection, jmh

We always hear "reflection is slow, don't use reflection in Java". Just today there was [an article on Reddit's /r/java](https://www.reddit.com/r/java/comments/4wkzck/performance_cost_of_reflection/)  purportedly showing that reflection is ~10x slower than calling the getters directly.

Fortunately [the author](https://blog.frankel.ch/performance-cost-of-reflection/) provided [source code](https://github.com/nfrankel/reflection-performance). Unfortunately he committed a couple of mistakes:

- He was reallocating the object on every run. So the benchmark was in fact measuring allocation + access
- The result could be potentially eliminated by dead-code-elimination. In fact I think that was happening with the direct call to getters, that's why they were so insanely fast
- For reflecting he was getting the field at every iteration, instead of getting it once
- Also, it was measuring different things - calling a getter vs. accessing private fields

I fixed all these up (plus added [ReflectASM](https://github.com/EsotericSoftware/reflectasm) recommended by Reddit) and the results are:

![Reflection Benchmark Results Candle-Stick graph](/images/reflection_graph.png)

As you can see reflection is only ~3x slower than direct calls and using ReflectASM you get ~90% of the performance. There is also the MethodHandle option form Java 8 which I didn't test.

In conclusion: benchmarking is tricky. Selecting JMH is a good first step, but by no means guarantees success. Also, don't fear reflection. Don't abuse it, but it can be a good tool when needed.
