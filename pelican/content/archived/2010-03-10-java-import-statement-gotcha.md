Title: Java import statement gotcha
Date: 2010-03-10 13:49
Author: Attila-Mihaly Balazs
Tags: programming, java
Slug: java-import-statement-gotcha
Status: published

![190774444\_2687512fb9\_o](http://lh5.ggpht.com/_hrvCBhtWhJ4/S5eHUrNP70I/AAAAAAAACOE/aeCTbllzGiE/190774444_2687512fb9_o%5B2%5D.jpg?imgmax=800 "190774444_2687512fb9_o")
There is a lot of debate on the intertubes if one should or shouldn’t
use wildcard imports. I’m mostly indifferent to the discussion (mainly
because all the package references are resolved compile time – so there
is no performance overhead – and because today's IDE’s contain a lot of
smarts to help you figure out which is the actual class being
referenced), but here is something interesting I discovered recently:

Lets say that we have two classes with the same name in different
packages:

    package foo;

    public class Foo {
        public static void print() {
            System.out.println("Foo");
        }
    }

</code>

    package bar;

    public class Foo {
        public static void print() {
            System.out.println("Bar");
        }
    }

</code>

Now create a test class in the bar package:

    package bar;

    import foo.*;

    public class Test {
        public static void main(String[] args) {
            Foo.print();
        }
    }

</code>

Question: what will this class print out? The answer is – surprisingly
for me - “Bar”. It seems that the Java compiler (tested with 1.6u18, but
this is probably the same with other versions – although I’m not sure
about alternative implementations like GCJ) uses the following order to
determine the canonical class name:

1.  Classes which are explicitly imported
2.  Classes which are in the current package
3.  Classes imported with wildcards

Just something to know about.

Picture taken from [salimfadhley's
photostream](http://www.flickr.com/photos/salimfadhley/) with
permission.

PS. Amusing sidenote: when you [search for import on
Flickr](http://www.flickr.com/search/?q=import&l=commderiv&ss=2&ct=6&mt=all&w=all&adv=1),
a lot of “babe” photos come up, even with safe search on. Is “import” a
codeword for something? :-)
