Title: Updated YARPG
Date: 2010-04-09 15:10
Author: Attila-Mihaly Balazs
Tags: security, programming, passwords, javascript
Slug: updated-yarpg
Status: published

![3273756192\_6008cde373\_b](http://lh6.ggpht.com/_hrvCBhtWhJ4/S78ZSy3nSpI/AAAAAAAACPQ/bqrf4VZA3h4/3273756192_6008cde373_b5.jpg?imgmax=800 "3273756192_6008cde373_b")
This has been sitting in my queue for some time: almost four years ago
(it’s incredible how time flies!) – amongst the first posts I’ve
published on the blog – I’ve written [a random password generator in
Javascript](http://hype-free.blogspot.com/2006/10/javascript-password-generator.html)
which I’ve named YARPG (for “Yet Another Random Password Generator”).
The advantages to using it are the same as they were back then:

-   Customizable (password length, types of characters included, etc)
-   Secure (it doesn’t communicate over the network, hence no need for
    SSL)
-   Fully reviewable (as opposed to server-based solutions, where you
    have to trust the server)

The only flaw it had (as pointed out by a commenter) was the fact that
passwords didn’t always include all the characters you’ve selected (ie.
the checkboxes represented “possible” not “mandatory” characters, which
was a little counter-intuitive).

I’ve thought about how to create passwords which included at least one
character from each set. My first ideas were around generating a
password, then checking that it contained at least one character from
each set and if not, replacing some of the characters with ones from the
missing set. However this train of thought quickly ran into problems
when I had to decide which character to replace. Choosing something
fixed (like the first one, last one, etc) is too predictable. If I
choose a random one, I run the risk of overwriting previous change. So
finally I realized that there is a simple solution: just re-generate the
password until it satisfies all of the constraints. Although this might
seem like a brute-force solution, in practice its speed is
indistinguishable from a constant-time solution.

Below you have the new and improved YARPG:

<style type="text/css">
<!--<br />
div.password_generator_noscript {<br />
 background-color: #ff7997;<br />
 border: thin dashed;<br />
}</p>
<p>div#generated_password {<br />
 font-family: monospace;<br />
 font-weight: bold;<br />
}</p>
<p>div#password_generator_div input {<br />
}</p>
<p>div#password_generator_div label {<br />
 width: 10em;<br />
}<br />
--></style>
<noscript>
</noscript>
<table id="password_generator_div" summary="random password generator with javascript">
<tbody>
<tr>
<td>
<label for="password_length">Password length:</label>

</td>
<td>
<input id="password_length" size="size" name="password_length"></input>

</td>
</tr>
<tr>
<td>
<label for="password_include_letters">Include letters</label>

</td>
<td>
<input id="password_include_letters" checked="checked" type="checkbox" name="password_include_letters"></input>

</td>
</tr>
<tr>
<td>
<label for="password_include_mixed_case">Include mixed case</label>

</td>
<td>
<input id="password_include_mixed_case" checked="checked" type="checkbox" name="password_include_mixed_case"></input>

</td>
</tr>
<tr>
<td>
<label for="password_include_numbers">Include numbers</label>

</td>
<td>
<input id="password_include_numbers" checked="checked" type="checkbox" name="password_include_numbers"></input>

</td>
</tr>
<tr>
<td>
<label for="password_include_punctuation">Include punctuation</label>

</td>
<td>
<input id="password_include_punctuation" type="checkbox" name="password_include_punctuation"></input>

</td>
</tr>
<tr>
<td>
<label for="password_include_all_printable">Include all printable
characters</label>

</td>
<td>
<input id="password_include_all_printable" type="checkbox" name="password_include_all_printable"></input>

</td>
</tr>
<tr>
<td>
<label for="password_quantity">Quantity</label>

</td>
<td>
<select id="password_quantity" name="password_quantity">
<option value="1">1</option> <option value="2">2</option>
<option value="3">3</option> <option value="4">4</option>
<option value="5">5</option> <option value="6">6</option>
<option value="7">7</option> <option value="8">8</option>
<option value="9">9</option> <option value="10">10</option>
<option value="11">11</option> <option value="12">12</option>
<option value="13">13</option> <option value="14">14</option>
<option value="15">15</option> <option value="16">16</option>
<option value="17">17</option> <option value="18">18</option>
<option value="19">19</option> <option value="20">20</option>
<option value="21">21</option> <option value="22">22</option>
<option value="23">23</option> <option value="24">24</option>
<option value="25">25</option> <option value="26">26</option>
<option value="27">27</option> <option value="28">28</option>
<option value="29">29</option> <option value="30">30</option>
<option value="31">31</option> <option value="32">32</option>
<option value="33">33</option> <option value="34">34</option>
<option value="35">35</option> <option value="36">36</option>
<option value="37">37</option> <option value="38">38</option>
<option value="39">39</option> <option value="40">40</option>
<option value="41">41</option> <option value="42">42</option>
<option value="43">43</option> <option value="44">44</option>
<option value="45">45</option> <option value="46">46</option>
<option value="47">47</option> <option value="48">48</option>
<option value="49">49</option> <option value="50">50</option>
<option value="51">51</option> <option value="52">52</option>
<option value="53">53</option> <option value="54">54</option>
<option value="55">55</option> <option value="56">56</option>
<option value="57">57</option> <option value="58">58</option>
<option value="59">59</option> <option value="60">60</option>
<option value="61">61</option> <option value="62">62</option>
<option value="63">63</option> <option value="64">64</option> </select>

</td>
</tr>
<tr>
<td colspan="2">
<button id="generate_password_button">
Generate

</button>
</td>
</tr>
<tr>
<td colspan="2">
<div id="generated_password">

</div>

</td>
</tr>
</tbody>
</table>
<p>
<script language="JavaScript" type="text/javascript"><!--<br />
var yajrpg = {<br />
    //puts each character from the string str in arr and returns a new array<br />
    PushArray : function (arr, str) {<br />
        var a = [];<br />
        for (var i = 0; i < str.length; i++)<br />
            a[a.length] = str.charAt(i);<br />
        arr[arr.length] = a;<br />
        return arr;<br />
    },</p>
<p>addEvent : function (obj, evType, fn) {<br />
        //taken from: http://www.scottandrew.com/weblog/articles/cbs-events<br />
        if (obj.addEventListener){<br />
            obj.addEventListener(evType, fn, false);<br />
            return true;<br />
        } else if (obj.attachEvent){<br />
            var r = obj.attachEvent("on"+evType, fn);<br />
            return r;<br />
        } else {<br />
            return false;<br />
        }<br />
    },</p>
<p>CheckAllPrintable : function () {<br />
        if (!yajrpg.inited) return;</p>
<p>yajrpg.pass_letters.disabled = yajrpg.pass_printable.checked;<br />
        yajrpg.pass_uppercase.disabled = yajrpg.pass_printable.checked;<br />
        yajrpg.pass_numbers.disabled = yajrpg.pass_printable.checked;<br />
        yajrpg.pass_punctuation.disabled = yajrpg.pass_printable.checked;<br />
    },</p>
<p>GenerateRandomPasswords : function () {<br />
        if (!yajrpg.inited) return;</p>
<p>var pass_length = parseInt(yajrpg.pass_length.value);<br />
        if (pass_length < 1 || pass_length > 256) return false;</p>
<p>var needed_charsets = [];<br />
        if (yajrpg.pass_printable.checked) {<br />
            var print_chars = [];<br />
            for (var i = 32; i < 127; i++)<br />
                print_chars[print_chars.length] = String.fromCharCode(i);<br />
            needed_charsets[0] = print_chars;<br />
        } else {<br />
            if (yajrpg.pass_letters.checked) yajrpg.PushArray(needed_charsets, "qwertyuiopasdfghjklzxcvbnm");<br />
            if (yajrpg.pass_uppercase.checked) yajrpg.PushArray(needed_charsets, "QWERTYUIOPASDFGHJKLZXCVBNM");<br />
            if (yajrpg.pass_numbers.checked) yajrpg.PushArray(needed_charsets, "0123456789");<br />
            if (yajrpg.pass_punctuation.checked) yajrpg.PushArray(needed_charsets, ":;,.?!");<br />
        }</p>
<p>if (0 == needed_charsets.length) return false;</p>
<p>var pass_quantity = parseInt(yajrpg.pass_quantity.options[yajrpg.pass_quantity.selectedIndex].value);</p>
<p>if (pass_length < needed_charsets.length) pass_length = needed_charsets.length;</p>
<p>var result = "";<br />
        for (var i = 0; i < pass_quantity; i++) {<br />
            var p;<br />
            while (true) {<br />
                p = [];<br />
                var used_charsets = [];<br />
                for (var j = 0; j < needed_charsets.length; ++j) used_charsets[j] = false;</p>
<p>for (var j = 0; j < pass_length; ++j) {<br />
                    var k = Math.floor(Math.random()*needed_charsets.length);<br />
                    var available_chars = needed_charsets[k];<br />
                    p[j] = available_chars[Math.floor(Math.random()*available_chars.length)];<br />
                    used_charsets[k] = true;<br />
                }</p>
<p>var all_charsets_used = true;<br />
                for (var j = 0; j < needed_charsets.length; ++j) all_charsets_used = all_charsets_used && used_charsets[j];<br />
                if (all_charsets_used) break;<br />
            }</p>
<p>for (var j = 0; j < pass_length; j++) {<br />
                var ch = p[j];<br />
                if ("<" == ch) ch = "<";<br />
                if (">" == ch) ch = ">";<br />
                result += ch;<br />
            }<br />
            result += '<br  />';<br />
        }<br />
        yajrpg.gen_pass_div.innerHTML = result;</p>
<p>return false;<br />
    },</p>
<p>CheckPasswordLength : function () {<br />
        if (!yajrpg.inited) return;</p>
<p>var pass_length = parseInt(yajrpg.pass_length.value);<br />
        if ((pass_length < 1) || (pass_length > 256))<br />
            yajrpg.pass_length.style.backgroundColor = 'red';<br />
        else<br />
            yajrpg.pass_length.style.backgroundColor = '';<br />
    },</p>
<p>initAfterLoad : function () {<br />
        //get the elements from the document<br />
        yajrpg.pass_letters = document.getElementById('password_include_letters');<br />
        yajrpg.pass_uppercase = document.getElementById('password_include_mixed_case');<br />
        yajrpg.pass_numbers = document.getElementById('password_include_numbers');<br />
        yajrpg.pass_punctuation = document.getElementById('password_include_punctuation');<br />
        yajrpg.pass_printable = document.getElementById('password_include_all_printable');<br />
        yajrpg.pass_length = document.getElementById('password_length');<br />
        yajrpg.gen_pass_div = document.getElementById('generated_password');<br />
        yajrpg.pass_quantity = document.getElementById('password_quantity');<br />
        yajrpg.gen_pass_button = document.getElementById('generate_password_button');</p>
<p>//check that we have all the elements<br />
        if (null == yajrpg.pass_letters || null == yajrpg.pass_uppercase || null == yajrpg.pass_numbers ||<br />
            null == yajrpg.pass_punctuation || null == yajrpg.pass_printable || null == yajrpg.pass_length ||<br />
            null == yajrpg.gen_pass_div || null == yajrpg.pass_quantity || null == yajrpg.gen_pass_button) return;</p>
<p>//fill up the select<br />
        for (var i = 1; i <= 64; i++)<br />
            yajrpg.pass_quantity.options[yajrpg.pass_quantity.options.length] = new Option(i, i);</p>
<p>//attach event handlers<br />
        if (!yajrpg.addEvent(yajrpg.gen_pass_button, 'click', yajrpg.GenerateRandomPasswords)) return;<br />
        if (!yajrpg.addEvent(yajrpg.pass_length, 'change', yajrpg.CheckPasswordLength)) return;<br />
        if (!yajrpg.addEvent(yajrpg.pass_printable, 'click', yajrpg.CheckAllPrintable)) return;</p>
<p>//display the form<br />
        var pass_generator = document.getElementById('password_generator_div');<br />
        if (null != pass_generator) pass_generator.style.display = ''; else return;</p>
<p>//everything has been initialized<br />
        yajrpg.inited = true;<br />
    },</p>
<p>//this initializes the object.<br />
    init : function () {<br />
        //postpone the final initialization after until the whole document has loaded<br />
        this.addEvent(window, 'load', this.initAfterLoad);<br />
        return this;<br />
    }<br />
}.init();<br />
//--></script>
I've also updated the [original
posting](http://hype-free.blogspot.com/2006/10/javascript-password-generator.html).
You can get the source code for it by looking at the source of this
webpage, or from my SVN repository:
[js\_password\_generator.html](http://code.google.com/p/hype-free/source/browse/trunk/js_password_generator.html).
Hopefully you find it useful!

*Picture taken from [cjc4454's
photostream](http://www.flickr.com/photos/cjc4454/) with permission.*
