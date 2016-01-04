Title: Computing the last digit of b^e efficiently
Date: 2010-03-15 13:20
Author: Attila-Mihaly Balazs
Tags: programming, mathematics
Slug: computing-last-digit-of-be-efficiently
Status: published

Geek PSA: Yesterday was PI day (3.14, get it?). Lets celebrate with this
spiked math comic:

[![](http://spikedmath.net/comics/197-memorizing-pi.png)](http://spikedmath.com/197.html)

Last week I saw the following problem which peaked my interest:

> Compute the last (decimal) digit of 2 raised to the power e where e
> might be very large.

We assume that we are talking about positive, integer exponents here.
The key observation here is that the last digit form a cycle:

    ...2 * 2 = ...4
    ...4 * 2 = ...8
    ...8 * 2 = ...6
    ...6 * 2 = ...2

So you can compute the last digit by calculating e MOD 4, which gives us
the position in the cycle. Next, I wondered if all the digits have this
cycling going on, so I searched around a little bit and found [this
page](http://cmsmcq.com/mib/images/expgraphs.html) which gives the cycle
for all ten digits. Now you can compute the last digit of the formula
b\^e with the following algorithm:

-   Take the last digit of b
-   compute e MOD (length of cycle for last digit of b)
-   return the given element of the cycle

This is very nice, since we can operate on arbitrary sized b, but we
still need to be able to perform the modulo operation on e, which might
be inconvenient if e is large. Fortunately we can make the following
observation:

-   The length of the cycle is either 1, 2 or 4
-   For x in [1,2,4] you have ...ab MOD x = ab MOD x (ie you can take
    only the last two digits and compute the modulo) since 100 is a
    multiple of both 2 and 4 (meaning that a number in the form of ...00
    will always be divisible by both 2 and 4, hence it contributes
    nothing to the modulo operation)

So here is the final algorithm which works quickly even for very large
values of b and e

-   Take the last digit of b
-   compute e MOD length\_of\_cycle by using the last two digits of e
-   return the given element of the cycle

Give it a try below if you have javascript enabled:

Math is fun :-).

<form>
<label for="large_num_base">b=</label><input id="large_num_base" onkeyup="&lt;br /&gt;
    var base = document.getElementById('large_num_base').value;&lt;br /&gt;
    var exp  = document.getElementById('large_num_exp').value;&lt;br /&gt;
    var f = function(b, e) {&lt;br /&gt;
        if (!/^\d+$/.test(b)) return 'Err';&lt;br /&gt;
        if (!/^\d+$/.test(e)) return 'Err';&lt;br /&gt;
        if (0 == e) return 1;&lt;/p&gt;
&lt;p&gt;b = b.substr(b.length-1); e = e.substr(e.length-2) - 1;&lt;br /&gt;
        var cycle = [ [0], [1], [2,4,8,6], [3,9,7,1], [4,6], [5], [6], [7,9,3,1], [8,4,2,6], [9] ];&lt;br /&gt;
        cycle = cycle[b];&lt;br /&gt;
        return cycle[e % cycle.length];&lt;br /&gt;
    };&lt;br /&gt;
    document.getElementById('last_digit').value = f(base, exp);&lt;br /&gt;
" style="text-align: right;"></input>  
  
<label for="large_num_exp">e=</label><input id="large_num_exp" onkeyup="document.getElementById('large_num_base').onkeyup()" style="text-align: right;"></input>  
  
<input id="last_digit" readonly="readonly" size="4" style="text-align: right;"></input>

</form>
Finally, I would like to leave you with the following question: is it
possible to efficiently compute an arbitrary digit of b\^e? My intuition
is that there are cycles in all of them, however they might be quite
long...
