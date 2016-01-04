Title: Using Jython from Maven
Date: 2011-10-13 18:16
Author: Attila-Mihaly Balazs
Tags: python, jython, maven, java
Slug: using-jython-from-maven
Status: published

*This blogpost was originally posted to* [*the Transylvania JUG
blog*](http://www.transylvania-jug.org/archives/303)*.*

On the surface it looks simple: just add the dependency and you can run
[the example
code](http://www.jython.org/archive/21/docs/embedding.html).

However what the `jython` artifact doesn’t get you are the standard
python libraries like `re`. This means that as soon as you try to do
something like the code below, it will error out:

    PythonInterpreter interp = new PythonInterpreter();
    try {
      interp.exec("import re");
    } 
    catch (PyException ex) {
      ex.printStackTrace();
    }

The solution? Use the `jython-standalone` artifact which includes the
standard libraries. An other advantage is that it has the latest release
(2.5.2) while `jython` lags two minor revisions behind (2.5.0) in Maven
Central. A possible downside is the larger size of the jar.

    org.python
    jython-standalone
    2.5.2
