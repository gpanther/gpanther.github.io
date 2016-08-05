Title: Benchmarking the cost of primitive operations on the JVM
Date: 2016-08-05 16:49
Author: Attila-Mihaly Balazs
Tags: java, performance, jvm, jmh, x86

(when are floating point operations faster than integer ones?)

I was listening to the [interview](http://cppcast.com/2015/10/andrei-alexandrescu/) with [Andrei Alexandrescu](http://erdani.com/) - of C++ and [D-lang](http://dlang.org/) fame (cheers homie! :-)) on CppCast when I heard something interesting: float divisions are supposed to be faster than integer ones on modern CPUs! So I had to dig into that.

## The setup

I whipped up some [JMH](http://openjdk.java.net/projects/code-tools/jmh/) benchmarks (the [sources](https://github.com/gpanther/jvm-primitive-ops-benchmarks) are on GitHub) and ran them on three machines:

* An older Xeon E5-2665
* An i7-4600U
* An i7-4750HQ

(Other factors - like memory, CPU count, exact JVM version, etc - are not that relevant to this discussion since this is strictly a single-threaded ALU benchmark)
 
## The answers

You can find the exact numbers in [the GitHub repository](https://github.com/gpanther/jvm-primitive-ops-benchmarks) and I also created [a Google Docs spreadsheet](https://docs.google.com/spreadsheets/d/10aayQ0hvYDI50t5Q4MB1E3Z4bgX2UIBBGG4y_I8Xhp8/edit?usp=sharing) to better visualize the results.

* What is the order (from a speed point of view) of integer operations?
  * They seem to fall into two categories div/mod and the rest, with the former being twice as slow as the later.
  * This seems to hold regardless of data type (byte / short / long / etc) or CPU (though the later CPUs are ~30% faster)

* Is computation on smaller integers (ie. byte / short / char) faster / slower / the same than on larger (int / long)?
  * In general in is the fastest, followed by long and the other types (byte / char / short)
  * For modulo (`%`) long is particularly slow

* The same question as above for floating point numbers: are calculations on float faster / slower / the same as on double?
  * For addition / subtraction they are the same speed (note that I only tested numbers which are of similar magnitude - so perhaps the results are different if rescaling is involved)
  * For division float was 30% to 50% faster (depending on the CPU model) than double (!)
  * The order of operations (in decreasing order of ops/s) seems to be:
    * addition / subtraction
    * multiplication (about the same speed)
    * division (about 30% to 50% slower)
    * modulo (30% to 50% slower than division)
    * multiplication / division on [denormal values](https://en.wikipedia.org/wiki/Denormal_number) - this is at least 50x (yes, times not percent!) slower 

* Back to the original question: can floating point division be faster than the integer one?
  * Amazingly yes! The benchmark shows that float division is ~30% faster than integer division (which is approximately the same speed as double division and both are 2x faster than long division)
  * This does not hold for related operations like multiplication (where they are approximately the same speed) and modulo (where int more than twice as fast as the others)

## The answers - part II

So this is it, right? Use float division? Lets apply this optimization to some real-world problems:

* [Vector multiplication](https://github.com/gpanther/jvm-primitive-ops-benchmarks/tree/master/src/main/java/net/greypanther/opbench/vecmult)
* [Interpolation search](https://github.com/gpanther/jvm-primitive-ops-benchmarks/tree/master/src/main/java/net/greypanther/opbench/search)

And the results are:

* For vector multiplication we indeed see a 2x to 5x performance gain when using float instead of int
* However for interpolation search we see the opposite: ints are ~30% _faster_ than floats

Why might that be?

My working theory is that _individual_ floating point divisions are (slightly) _slower_ than integer divisions. However: there are probably more ALUs in the CPU which can do floating point operations and if the operations can be pipelined (ie. they can be executed in parallel / there is no data dependency between them) the overall throughput is better.

In other cases - like with interpolation search - where we need the result of the individual division before we can progress, pipelineing doesn't help.

## Some conclusions

Do your own benchmarks! Don't trust a page on the internet! Things can change considerably with new CPU architectures / JVMs!

* Consider investing in hardware. There can be considerable performance gain in running on the latest vs. 3-4 year old hardware and it's a simple upgrade
* Store your data in int / float if it fits. Anything smaller hurts your arithmetic performance (but can help considerably if you're bottlenecked on memory bandwidth)
* Use the correct kind of data (floating point for simulations and integers for everything else - including monetary values which should be stored as multiples of 1/1000th of a cent)
* Don't use denormalized floating point numbers for multiplication / division if you can help it
  * Of course there is a lot more to floating point algorithms like [numerical stability](https://en.wikipedia.org/wiki/Numerical_stability) so thread lightly when mucking around with such algorithms

* Using shifts / masking where appropriate (for example multiplying / dividing by powers of two) is still a very worthwhile optimization (the JVM/JIT does this automatically when it can "see" the constant part - ie. there is no need to write `v >> 2` instead of `v / 4`)

