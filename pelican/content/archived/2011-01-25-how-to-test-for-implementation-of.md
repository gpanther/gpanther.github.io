Title: How to test for the implementation of toString()
Date: 2011-01-25 13:45
Author: Attila-Mihaly Balazs
Tags: espresso shots, unit tests, java, junit
Slug: how-to-test-for-implementation-of
Status: published

*Update*: This entry has been crossposted to the [transylvania-jug
blog](http://www.transylvania-jug.org/archives/165).

Problem statement: you have some value objects for which you implemented
toString() (for debugging purposes) and now you would like to test using
a unit test that these implementations exist.

Possible solutions:

1.  Use reflection to detect the existence of the method:

        boolean hasToStringViaReflection(Class<? ?> clazz) {
          Method toString;
          try { toString = clazz.getDeclaredMethod("toString"); }
          catch (NoSuchMethodException ex) { return false; }
          if (!String.class.equals(toString.getReturnType())) { return false; }
          return true;
        }

    <p>
    Advantage: no third party libraries needed. Also, no instance of the
    class is needed. Disadvantage: the actual code is not executed, so
    even trivial errors (like null dereferences) are not caught. Also,
    code coverage tools will report the lines as not covered.

2.  Compare the string returned by the toString method to the string
    returned by Object and expect them to be different. This uses
    [ObjectUtils](http://commons.apache.org/lang/api-2.6/org/apache/commons/lang/ObjectUtils.html#identityToString%28java.lang.Object%29)
    from Apache Commons Lang:

        boolean hasToStringViaInvocation(Object o) {
          return !ObjectUtils.identityToString(o).equals(o.toString());
        }

    <p>
    Advantage: the actual code is executed, so trivial errors are
    detected. Also the code will be "covered". Disadvantage: it requires
    an external library (however Commons Lang contains a lot of goodies,
    so it is sensible to add it most of the time). Also, it requires an
    instance of the class, so you need to be able to instantiate it.

3.  Don't use hand-coded methods at all, but rather some code-generation
    / AOP style programming like [Project
    Lombok](http://projectlombok.org/features/ToString.html).

Again, these methods are to be used for toString methods which have
debugging purpose only. In case the output of the method needs to
conform to some stricter rule, more checks need to applied.

The complete source code can be found on [Google
Code](http://code.google.com/p/hype-free/source/browse/trunk/espresso-shots/src/org/transylvania/jug/espresso/shots/d20110124/TestForToString.java)
under Public Domain or the BSD license.
