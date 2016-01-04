Title: Careful with that axe^H^H^H static, Eugene!
Date: 2009-08-31 17:36
Author: Attila-Mihaly Balazs
Tags: programming, java
Slug: careful-with-that-axehhh-static-eugene
Status: published

[![557403262\_2d8d8a3576\_b](http://lh6.ggpht.com/_hrvCBhtWhJ4/Spvf3tYUf6I/AAAAAAAABM0/GaKabjQsYJU/557403262_2d8d8a3576_b_thumb.jpg?imgmax=800 "557403262_2d8d8a3576_b")](http://lh3.ggpht.com/_hrvCBhtWhJ4/Spvf3ORzTWI/AAAAAAAABMs/-VfXTWIlD_A/s1600-h/557403262_2d8d8a3576_b%5B2%5D.jpg)
An other instance from the “bugs which will bite you” series:

    public class TestStatic {
        static class Foo {
            static Foo instance = new Foo();
            static String name = Foo.class.getName();
            
            public Foo() {
                System.err.println("Hello, my name is " + name);
            }
        }
        
        public static void main(String[] args) {
            System.err.println("Your name is what?\n"
                + "Your name is who?\n");
            
            new Foo();
        }

    }

</code>

Can you spot the bug? Hint, here is the output:

</p>
    Your name is what?
    Your name is who?

    Hello, my name is null
    Hello, my name is TestStatic$Foo

</p>
A final hint: here is what FindBugs reports on the third line:
[SI\_INSTANCE\_BEFORE\_FINALS\_ASSIGNED](http://findbugs.sourceforge.net/bugDescriptions.html#SI_INSTANCE_BEFORE_FINALS_ASSIGNED)

Yet an other reason to reduce your FindBugs count to zero before
releasing software!

Picture taken from [helena.40proof's
photostream](http://www.flickr.com/photos/76099968@N00/) with
permission.
