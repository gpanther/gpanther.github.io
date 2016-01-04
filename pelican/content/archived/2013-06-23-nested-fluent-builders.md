Title: Nested fluent builders
Date: 2013-06-23 15:26
Author: Attila-Mihaly Balazs
Slug: nested-fluent-builders
Status: published

*Crossposted from [the Transylvania JUG
website](http://www.transylvania-jug.org/archives/5692).*

Builders have become commonplace in current Java code. They have the
effect of transforming the following code:

``` {lang="java" escaped="true"}
new Foo(1, 5, "abc", false);
```

</code>

Into something like

``` {lang="java" escaped="true" line="1"}
Foo.builder()
  .count(1)
  .priority(5)
  .name("abc")
  .canonical(true)
  .build();
```

</code>

This has the advantage of being much easier to understand (as a downside
we can mention the fact that - depending on the implementation - it can
result in the creation of an additional object). The implementation of
such builders is very simple - they a list of "setters" which return the
current object:

``` {lang="java" escaped="true" line="1"}
public final class FooBuilder {
  private int count = 1;
  // ...

  public FooBuilder count(int count) {
    this.count = count;
    return this; 
  }

  public Foo build() {
    return new Foo(count, //...
  }
}
```

</code>

Of course writing even this code can become repetitive and annoying, in
which case we can use
[Lombok](http://projectlombok.org/features/experimental/Builder.html) or
other code generation tools. An other possible improvement - which makes
builder more useful for testing - is to add methods like random as
suggested in [this Java Advent
Calendar](http://www.javaadvent.com/2012/12/using-builder-pattern-in-junit-tests.html)
article. We can subclass the builder (into FooTestBuilder for example)
and only use the "extended" version in testing.

What can do however if our objects are more complex (they have
non-primitive fields)? One approach may look like this:

``` {lang="java" escaped="true" line="1"}
Foo.builder()
  .a(1)
  .b(2)
  .bar(Bar.builder().c(1).build())
  .buzz(Buzz.builder().build())
  .build();
```

</code>

We can make this a little nicer by overloading the bar / buzz methods to
accept instances of BarBuilder / BuzzBuilder, in which case we can omit
two build calls. Still, I longed for something like the following:

``` {lang="java" escaped="true" line="1"}
Foo.builder()
  .a(1)
  .b(2)
  .bar()
     .c(1).build()
  .buzz()
     .build()
  .build();
```

</code>

The idea is that the bar / buzz calls call start a new "context" where
we initialize the Bar/Buzz classes. "build" calls end the innermost
context, with the last build returning the initialized Foo object
itself. How can this be written in a typesafe / compiler verifiable way?

My solution is the following:

-   Each builder is parameterized to return an arbitrary type T from its
    build method
-   The actual return value is generated from a Sink of T
-   When using the builder at the top level, we use an IdentitySink with
    just returns the passed in value.
-   When using the builder in a nested context, we use a Sink which
    stores the value and returns the builder from "one level up".

Some example code to clarify the explanation from above can be found
below. Note that this code has been written as an example and could be
optimized (like making using a single instance of the IdentitySink,
having FooBuilder itself implementing the sink methods, etc).

Implementation of a leaf-level builder:

``` {lang="java" line="1"}
interface Sink {
  T setBar(Bar bar);
}

final class Bar {
  // ...
  public static BarBuilder builder() {
    return new BarBuilder(new Sink() {
      @Override
      public Bar setBar(Bar bar) { return bar; }
    });
  }
}

class BarBuilder {
  // ...

  protected BarBuilder(Sink sink) {
    this.sink = sink;
  }

  // ...

  public T build() {
    return sink.setBar(new Bar(c, d, fizz));
  }
}
```

Implementation of the root level builder:

``` {lang="java" line="1"}
class FooBuilder {
  // ...
  public BarBuilder setBar() {
    return new BarBuilder(new Sink() {
      @Override
      public Bar setBar(Bar bar) { 
        FooBuilder.this.bar = bar;
        return FooBuilder.this;
      }
    });
  }

  // ...
}
```

</code>

Conclusion: Java has some missing features (liked named parameters or
the ease of reuse provided by duck-typing). We can work around them
however nicely with some carefully crafted code (and we can put
repeating code into code generators to avoid having to write it over and
over again). In exchange we get a very versatile and good performing
cross-platform runtime.
