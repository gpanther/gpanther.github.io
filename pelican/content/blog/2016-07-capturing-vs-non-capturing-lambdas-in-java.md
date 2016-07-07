Title: Capturing vs. Non-Capturing Lambdas in Java
Date: 2016-07-06 19:22
Author: Attila-Mihaly Balazs
Tags: java

I was watching Peter Lawrey's talk about [Low latency Lambdas in Java 8](https://www.youtube.com/watch?v=vZngvuXk7PM)
where he posed the question: which of he following is a non-capturing lambda?

````
x -> System.out.println(x)
````

or

````
System.out::println
````

Naively I would have said that they both are but that the second form is preferred since it makes it harder to write
a capturing lambda (seemingly you don't have any variable references). However!

It turns out only the first one is non-capturing since the second one needs to capture `System.out`, even though it
is a `final static` field! (I guess it does this because finals in Java/JVM are not really final, so to achieve the
correct semantics in every corner-case it needs to capture the current field value. Then again the behavior didn't
change once I activated the ["finals are really final" experimental flag](http://shipilev.net/blog/2015/faster-atomic-fu/)
 - `-XX:+UnlockExperimentalVMOptions -XX:+TrustFinalNonStaticFields` - but that might be precisely because this is
is an experimental option and the optimizer is not fully aware of it).

Finally, is there a way to programatically determine if a lambda is capturing or non capturing? AFAIK there is no
_official_ way but there are some hacks:

If you have a lambda factory rather than a lambda instance, you can just call it twice and see if you get the same
instance:

````
boolean isCapturingFromFactory(Supplier<?> factory) {
	return factory.get() != factory.get();
}
````

If you only have the lambda instance, you can check using reflection if there are any private final fields on it
(which are used to capture the required values during construction time):

````
private static boolean isCapturing(Object o) {
	Class<?> clazz = o.getClass();

	if (!clazz.toString().contains("$Lambda$")) {
		throw new IllegalArgumentException("Not a lambda!");
	}

	for (Field field : clazz.getDeclaredFields()) {
		int modifiers = field.getModifiers();
		if (Modifier.isFinal(modifiers) && Modifier.isPrivate(modifiers)) {
			return true;
		}
	}

	return false;
}
````

