Title: Writing beautiful code - not just for the aesthetic value
Date: 2012-11-06 14:33
Author: Attila-Mihaly Balazs
Slug: writing-beautiful-code-not-just-for
Status: published

*This article was originally published in [the 6th edition of
TodaySoftMag in
Romanian](http://www.todaysoftmag.com/article/ro/6/A_scrie_cod_frumos_-_dincolo_de_valoarea_estetica_159)
and on the [Transylvania JUG blog in
English](http://www.transylvania-jug.org/archives/5477). Reprinted here
with the permission of the author / magazine.*

<p>
<center>
<iframe src="https://docs.google.com/presentation/embed?id=1fC4qeDc4zkKGaLZBMrRdgmRMuoDw4KeYmmJAZvVVFLY&amp;start=false&amp;loop=false&amp;delayms=3000" frameborder="0" width="480" height="389" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true">
</iframe>
</center>
</p>
Most mainstream programming languages contain a large set of features
and diverse standard libraries. Because of this it becomes important to
know not only “how” you can achieve something (to which there are
usually several answers) but also “what is the recommended way”.

In this article I will argue that knowing and following the recommended
ways of coding doesn’t only yield shorter (easier to write), easier to
read, understand and maintain code but also prevents programmers from
introducing a lot of bugs.

This particular article needs a drop of Java language knowledge to
savour, but the fundamental idea can be generalized to any programming
language: there is more to using a language efficiently than just
knowing the syntax.

<span id="h.71vcwrw1xmys"></span></a>Example 1: Double Trouble
--------------------------------------------------------------

Lets start with a snippet of code: what does it print out?

    Double d1 = (5.0d - 5.0d) *  1.0d;
    Double d2 = (5.0d - 5.0d) * -1.0d;
    System.out.println(d1.equals(d2));

</code>

What about the following one?

    double d1 = (5.0d - 5.0d) *  1.0d;
    double d2 = (5.0d - 5.0d) * -1.0d;
    System.out.println(d1 == d2);

</code>

The answer seems to be clear: in both cases we multiply zero with
different values (plus and minus one respectively), thus the result
should be zero which should compare as equal regardless of the
comparison method used (calling the equals method on objects or using
the equality operator on the primitive values).

If we run the code, the result might surprise us: the first one displays
false while the second one displays true. What’s going on? On one level
we can talk the technical reasons behind this result: floating point
values are represented in Java (and many other programming languages)
using the sign-and-magnitude notation defined in the IEEE Standard 754.
Because of this technical detail both “plus zero” and “minus zero” can
be represented by variables of this type. And the “equals” method on
Double (and Float) objects in Java considers these values to be
distinct.

On another level however we could have avoided this problem entirely by
using the primitive values as shown in the second code snippet and as
suggested by Item 49 in the Effective Java book^<span
id="ftnt_ref1">[[1]](#ftnt1)</span>^: Prefer primitive types to boxed
primitives. Using primitive types is also more memory efficient and
saves us from having to create special cases for the null value.

Sidenote: we have a similar situation with the BigDecimal class^<span
id="ftnt_ref2">[[2]](#ftnt2)</span>^ where values scaled differently
don’t compare as equal. For example the following snippet also prints
false:

    BigDecimal d1 = new BigDecimal("1.2");
    BigDecimal d2 = new BigDecimal("1.20");
    System.out.println(d1.equals(d2));

</code>

The answer in this case (given that there is no primitive equivalent for
this class) would be to use the compareTo method and assert that it
returns zero instead of using the equals method (a method which can also
be used to solve the conundrum in the Double/Float case if we are not
worried about nulls).

<span id="h.t3ulkiuv7mcw"></span></a>Example 2: Where is my null at?
--------------------------------------------------------------------

What does the following snippet of code print out?

    Double v = null;
    Double d = true ? v : 0.0d;
    System.out.println(d);

</code>

At first glance we would say: null, since the condition is true and v is
null (and null can be assigned to a reference of any type, so we are
allowed to use it). The actual result is however a NullPointerException
at the second line. This is because the right-hand type of the
assignment is actually double (the primitive type) not Double (as we
would expect) which is silently converted into Double (the boxed type).
The generated code looks like this:

    Double d = Double.valueOf(true ? v.doubleValue() : 0.0d);

</code>

This behavior is described in the Java Language Specification^<span
id="ftnt_ref3">[[3]](#ftnt3)</span>^:

“If one of the second and third operands is of primitive type T, and the
type of the other is the result of applying boxing conversion (§5.1.7)
to T, then the type of the conditional expression is T.”

I would venture to guess that not many of us have read the JLS in its
entirety and even if we would have read it, we might not have realized
the implications of each phrase. The recommendation from EJ2nd mentioned
at the previous example saves us again: we should use primitive types.
We can also draw a parallel with Item 43: Return empty arrays or
collections, not nulls. Would we have used a “neutral element”, which is
analogous to using empty arrays/collections, the problem would not have
appeared. (The neutral element would be 0.0d if we use the value later
in summation or 1.0d if we use it in multiplication.)

<span id="h.1mt6ca4376w9"></span></a>Example 3: We come up empty
----------------------------------------------------------------

What is the difference between the following two conditions?

    Collection items;
    if (items.size() == 0) { ... }
    if (items.isEmpty()) { ... }

</code>

One could argue that they do exactly the same thing as being empty is
equivalent to having zero items. Still, the second condition is easier
to understand (we can almost read it out loud: “if items is empty then
…”). But there is more: in some cases it can be much, much faster. Two
examples from the Java standard libraries where the time needed to
execute “size” grows linearly with the number of elements in the
collection while “isEmpty” returns in constant time:
ConcurrentLinkedQueue^<span id="ftnt_ref4">[[4]](#ftnt4)</span>^ and the
view sets returned by TreeSet’s^<span
id="ftnt_ref5">[[5]](#ftnt5)</span>^ headSet/tailSet methods. And while
the documentation for the first mentions this fact, it doesn’t for the
second.

This is yet another example how nicer code is also faster.

<span id="h.orqngpa6ggt9"></span></a>Example 4: Careful with that static, Eugene!
---------------------------------------------------------------------------------

What will the following snippet of code print out?

    public final class Test {
            private static final class Foo {
                    static final Foo INSTANCE = new Foo(); // 2
                    static final String NAME = Foo.class.getName(); // 3
                    Foo() {
                            System.err.println("Hello, my name is " + NAME);
                    }
            }
            public static void main(String[] args) {
                    System.err.println("Your name is what?\nYour name is who?\n");
                    new Foo(); // 1
            }
    }

</code>

It will be

    Your name is what?
    Your name is who?

    Hello, my name is null
    Hello, my name is Test$Foo

</code>

The (probably) unexpected null value happens because we obtain a
reference to a partially constructed object:

-   We start to create an instance of Foo at point 1
-   This being the first reference to Foo, the JVM loads it and starts
    to initialize it
-   Initializing Foo involves initializing all its static fields
-   The initialization of the first static field contains a call to the
    constructor at point 2 which is dutifully executed
-   At this point the NAME static field is not yet initialized, so the
    constructor will print out null

This code demonstrates that static fields can be confusing and we
shouldn’t use them for things other than constants (but even then we
should evaluate if the constant is not better declared as an Enum). By
the same token we should also avoid singletons which make our code
harder to test (thus avoiding them will make the code easier to test).

We should however favor static member classes over non-static ones (Item
22 in EJ2nd). Static classes in Java are entirely distinct conceptually
from static fields and it is unfortunate that the same word was used to
describe them both.

We should also run static analysis tools on our code and verify their
output frequently (ideally at every commit). For example the bug
presented is caught by Findbugs^<span
id="ftnt_ref6">[[6]](#ftnt6)</span>^ and tools incorporating Findbugs.

<span id="h.26ynxgfuhslr"></span></a>Example 5: Remove old cruft
----------------------------------------------------------------

Name four things wrong with the following snippet:

    // WRONG! DON’T DO THIS!
    Vector v1;
    ...
    if (!v1.contains(s)) { v1.add(s); }

</code>

They would be:

-   The wrong container type is used. We clearly want to have each
    string present at most once which suggests using a Set
-   which has the benefits of shorter and faster code (the above method
    gets linearly slower with the number of elements)
-   Doesn’t use generics
-   It unnecessarily synchronizes access to the structure if it is only
    used from a single thread
-   If the structure is actually used from multiple threads, the code is
    not thread safe, only “exception safe” (as in: no exceptions will be
    raised, but the data structure can be silently corrupted possibly
    creating a lot of headache downstream)

All of these can be avoided by dropping Vector and its siblings
(Hashtable, StringBuffer) and using the Java Collection Framework
(available for 14 years^<span id="ftnt_ref7">[[7]](#ftnt7)</span>^) with
generics (available for 8 years^<span
id="ftnt_ref8">[[8]](#ftnt8)</span>^).

<span id="h.t7tt7vdn4ji9"></span></a>Conclusion
-----------------------------------------------

There are many more examples one could give, but I think the point is
well made that knowing a programming language means more than just
knowing the syntax at a basic level. I’m urging you if you are using
Java: get yourself a copy “Effective Java, 2nd edition” and “Java™
Puzzlers: Traps, Pitfalls, and Corner Cases” each and read through them
if you haven’t done so already. Also, use static analysis on your code
(Sonar^<span id="ftnt_ref9">[[9]](#ftnt9)</span>^ is a good choice in
this domain) and consider fixing the issues signaled by it, or at least
read up on them.

Again, the conclusions is similar for other languages:

-   Try reading up on best practices/idiomatic ways to write code in the
    given language. For example for Perl the best book currently is
    “Modern Perl^<span id="ftnt_ref10">[[10]](#ftnt10)</span>^” by
    chromatic
-   Look to see if there is a good quality static analysis / lint
    program for your language. For Perl there is Perl::Critic^<span
    id="ftnt_ref11">[[11]](#ftnt11)</span>^, for Python there is
    pep8^<span id="ftnt_ref12">[[12]](#ftnt12)</span>^ and pylint^<span
    id="ftnt_ref13">[[13]](#ftnt13)</span>^, all of which are free and
    open source

Being good a programmer (or an architect, or a business analyst, etc) is
process of lifelong learning and these are the tools which can help us
truly learn a programming language.

------------------------------------------------------------------------

<div>

<span id="ftnt1">[[1]](#ftnt_ref1)</span>Joshua Bloch: Effective Java,
Second Edition. ISBN: 0321356683

</div>

<div>

<span
id="ftnt2">[[2]](#ftnt_ref2)</span><http://docs.oracle.com/javase/7/docs/api/java/math/BigDecimal.html>

</div>

<div>

<span
id="ftnt3">[[3]](#ftnt_ref3)</span><http://docs.oracle.com/javase/specs/jls/se7/html/jls-15.html#jls-15.25>

</div>

<div>

<span
id="ftnt4">[[4]](#ftnt_ref4)</span><http://docs.oracle.com/javase/7/docs/api/java/util/concurrent/ConcurrentLinkedQueue.html#size()>

</div>

<div>

<span
id="ftnt5">[[5]](#ftnt_ref5)</span><http://docs.oracle.com/javase/7/docs/api/java/util/TreeSet.html>

</div>

<div>

<span
id="ftnt6">[[6]](#ftnt_ref6)</span><http://findbugs.sourceforge.net/bugDescriptions.html#SI_INSTANCE_BEFORE_FINALS_ASSIGNED>

</div>

<div>

<span
id="ftnt7">[[7]](#ftnt_ref7)</span><http://en.wikipedia.org/wiki/Java_version_history#J2SE_1.2_.28December_8.2C_1998.29>

</div>

<div>

<span
id="ftnt8">[[8]](#ftnt_ref8)</span><http://en.wikipedia.org/wiki/Java_version_history#J2SE_5.0_.28September_30.2C_2004.29>

</div>

<div>

<span id="ftnt9">[[9]](#ftnt_ref9)</span><http://www.sonarsource.org/>

</div>

<div>

<span
id="ftnt10">[[10]](#ftnt_ref10)</span><http://www.onyxneon.com/books/modern_perl/index.html>

</div>

<div>

<span
id="ftnt11">[[11]](#ftnt_ref11)</span><http://search.cpan.org/~thaljef/Perl-Critic-1.118/lib/Perl/Critic.pm>

</div>

<div>

<span
id="ftnt12">[[12]](#ftnt_ref12)</span><http://pypi.python.org/pypi/pep8>

</div>

<div>

<span
id="ftnt13">[[13]](#ftnt_ref13)</span><http://pypi.python.org/pypi/pylint>

</div>
