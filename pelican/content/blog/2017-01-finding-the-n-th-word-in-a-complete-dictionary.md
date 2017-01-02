Title: Finding the N-th word in a complete dictionary
Date: 2017-01-02 13:28
Author: Attila-Mihaly Balazs
Tags: algorithm

## Problem statement

Find the `N`-th word in a dictionary which contains all the words that can be generated from a given alphabet of length at most `M` (and sorted by the conventional dictionary sorting rule / [lexicographical order](https://en.wikipedia.org/wiki/Lexicographical_order)).

As a short detour: why did I become interested in it? It was during my investigation of the upper limit for the number of strings formed from a given alphabet that can be encoded in a given number of bits. Even more concretely: what is the upper limit for the length of a DNA/RNA string formed from nucleotides (ie. a string with alphabet `[A,C,G,T]`) that can be encoded on 64 bits. Note: the problem statement that we need a codec (ie. both enCOding and DECoding, so we'll solve a bit more generic problem than just the one-way one described in the title).

The first solution which came to mind was to use some bits for the length and the remaining bits to encode the nucleotides (2 bit / nucleotide) however the question remained: how many bits for the length? And is the solution optimal?

So finally I came up with the following formulation: consider that we have a dictionary of all the possible nucleotide strings for length at most `M`. Now let the 64 bit value just be an index in this dictionary. This is guaranteed to be the optimal solution (if we assume that the probability of occurrence for every string is the same). Now we need three things:

1. what is the largest value of `M` for which the index can be stored on 64 bits?
2. a time and space efficient way (ie. not generating the entire dictionary and keeping it in memory for lookup) to get the index of a given string (the enCOde step)
3. the same to get the word at a given index (the DECode step)

There is also a somewhat related problem on Project Euler ([24: Lexicographic permutations](https://projecteuler.net/problem=24)) - that wasn't the inspiration though, I found out about it later.

## Some initial observations

Just by writing out the complete set of words of length at most `M` formed from a given alphabet we can make some observations. For example consider the alphabet `[A,B]` and write out:

- the words of length 0: `''` (the empty string)
- the words of length 1: `A` and `B`
- the words of length 2: `AA`, `AB`, `BA` and `BB`

So pretty quickly we can see that for a given alphabet and a given length we have exactly `len(alphabet) ** length` possible words (where `**` is the exponentiation operator - ie. `a ** b` is the b-th power of a), since: we have `length` positions, at each position we can have one of the `len(alphabet)` characters, thus the total possibilities are `len(alphabet) * len(alphabet) * ... ` `length` times which is `len(alphabet)` to power `length`.

After this we can ask "how many strings of length less than or equal to `M` are there"? (question 1 from the initial problem statement).  This is simply `sum(len(alphabet) ** i for i in [0, M])`, also known as the [geometric progression](https://en.wikipedia.org/wiki/Geometric_progression#Derivation): `(1 - La ** M) / 1 - La` where `La = len(alphabet)`.

So for example if we have the alphabet `[A, C, G, T]` and 64 bits available we can encode [at most 32 characters](http://www.wolframalpha.com/input/?i=%28%281-4%5Em%29+%2F+%281-4%29%29+%3C+%282%5E64-1%29) according to Wolfram Alpha.

## Finding the index of a string

To find this we just need to count how many strings there are in the dictionary before our string (remember the dictionary is in lexicographical order).

A concrete example: our dictionary contains all the words of length at most 3 (`M=3`) formed from the alphabet `[A, B]`. What is the index of the word `BA`? (we consider that index 0 is `''` - the empty string, index 1 is `A`, index 2 is `AA` and so on).

What is the position of `BA` in our dictionary?

If we would only have words of length _exactly_ `K` we could compute this by considering `BA` a number in base 2 (binary) where `A=0` and `B=1`, transform it to base 10 and have our answer (ie `BA` -> `10b` -> `2` -> `BA` is at position 2 - or is the 3rd word - in the dictionary `AA, AB, BA, BB`).

However our dictionary contains all words of length _exactly_ 0, 1, 2 and 3. So just consider each in turn!

In a dictionary containing the words from the alphabet `[A, B]` of exactly length:

- `K=0`: `BA` would have index 1
- `K=1`: `BA` would have index 2 which is the same as `indexOf(B) + 1`
- `K=2`: `BA` would have index 2
- `K=3`: `BA` would have index 10, which is the same as `indexOf(BAA)`

So, to find the index of a string:

- Go from 0 to `M` (the maximum length allowed for words in our dictionary)
- Generate a word of length `K` from our word by either (assuming our strings are zero indexed):
  - Taking the characters `0` to `K` (exclusive) if `K < len(word)`
  -  Padding the word with the _first character of the alphabet_ up to length `K`
- Finding the index of this (sub)word in a dictionary that contains words of length exactly `K` by considering the (sub)word as a value written in base `La` (`La == length(alphabet)`). Add 1 if we're in the first case since the longer word would come after the shorter ones.
- Sum up all the values

Or in [Python 3 code](https://github.com/cdman/nth-element-of-dictionary/blob/master/nth_element.py#L83):

```python
def indexOf(self, word):
    assert len(word) <= self.__max_len
    result = 0
    for i in range(0, self.__max_len + 1):
        if i < len(word):
            subword = word[:i]
            result += self.__valueInBaseN(subword) + 1
        else:
            subword = word + (i - len(word)) * self.__alphabet[0]
            result += self.__valueInBaseN(subword)
    return result
```

## Finding the N-th string

Finally getting at the problem stated in the title. For this I noted how the dictionary can be constructed for length `M`:

- the dictionary for `M=0` is just `''` (the empty string) and for `M=1` the empty string plus the alphabet itself.
- for `M>1` take the dictionary for `M-1` and prefix it with each of the characters from the alphabet. Finally add the empty string as the first element.

So for example if we have `[A, B]` as the alphabet then:

- the dictionary for `M=1` is `0: '', 1: A, 2: B`
- to construct the dictionary for `M=2` we replicate the above dictionary 2 times, first prefixing it with `A`, then with `B` and finally we add the empty string in front:

```
0: ''  1: A    4: B
       2: AA   5: BA
       3: AB   6: BB
```

This suggests an algorithm for finding the solution:

- take the value. Decide in "column" it would be.
  - you know the number of words in each column: `len(dictionary) - 1 / len(alphabet)`
  - `len(dictionary)` is `sum(len(alphabet) ** i for i in [0, K])` (see the initial observations)
  - this can also be precomputed for efficiency
- the column index gives you letter index in the alphabet
- now subtract from the value the index of the first word in the given column. If you get 0, stop.
- Otherwise make `K` one less and look up the new value in the dictionary of length at most `K`.

A small worked example:

- lets say we have `[A, B]` as the alphabet and `M=2`. We want to find the word at 5 (which is `BA` if you take a peak at the table above). So:
- in each column we have 3 words, so 5 is in the 2nd row (the row with index 1) which gives us "B" as the first letter
- now subtract 4 (the index of the first word in the 2nd column - `B`) from 5 which leaves us with 1
- now find the word with index 1 in a dictionary with `M=1` which is "A"
- thus the final word is "BA"

Or in [Python 3 code](https://github.com/cdman/nth-element-of-dictionary/blob/master/nth_element.py#L62):

```python
def wordAt(self, index):
    assert 0 <= index <= self.__lastIndex
    result, current_len = '', self.__max_len
    while index > 0:
        words_per_column = self.__wordsPerLetterForLen[current_len]
        column_idx = (index - 1) // words_per_column
        result += self.__alphabet[column_idx]
        index_of_first_word_in_col = 1 + column_idx * words_per_column
        index -= index_of_first_word_in_col
        current_len -= 1
    return result
```
Note: you can find a different algorithm to do the same on [math.stackexchange.com](http://math.stackexchange.com/questions/195736/how-to-get-the-n-th-word-in-a-sequence), however I found the above to be visually more intuitive.

## Can we do it simpler?

So we solved the initial problem (both the one stated in the title and the one which motivated this journey) however it took over a thousand words to describe and justify it. Can we do simpler? Turns out yes! We just need abandon our attachment to the lexicographical order and say that as long as we have a bijective encoding and decoding function with the property `decode(encode(word)) == word` we are satisfied.

A simple and efficient function is the transformation of the word from base `La` (length of alphabet) to base 10 and vice-versa. For example if we have `[A, C, G, T]` as the alphabet and `GAT` as the word we can do:

- encode: `2*(4**2) + 0*(4**1) + 3*(4**0)` which is 33
- decode: 33 is written as powers of 4 as above and 2, 0, 3 corresponds to `GAT`

Again, the ordering will not be lexicographical (`A, AA, AB, ...`) but rather a numerical-order kind-of (`A, B, AA, AB, ...`) but the algorithm is much simpler and in the case that `La` is a power of two, very efficient to implement on current CPUs since division / remainder can be done using bit-shifts / masking.

## More speculation

I didn't actually want to encode DNA/RNA sequences, but rather mutations/variations which are pair of sequences (something like `G -> TC` or `GT -> ''`).  Now I could just divide the 64 bits into two 32 bit chunks but the same initial question would arise: is this the most optimal way for encoding?

So we go the same solution: what if we would have a dictionary of all the variants (`'' -> A, '' -> AA, ...`) and just index into it. How would we construct such a dictionary and how would we order it?

Turns out there is an algorithm inspired by the proof that [there are the same number of natural numbers as there are rational ones](https://en.wikipedia.org/wiki/Rational_number#Properties). However that doesn't give us a way to find the N-th element in the sequence but a Calkin–Wilf sequence [does](https://en.wikipedia.org/wiki/Calkin%E2%80%93Wilf_tree#Breadth_first_traversal).

So we can have the following algorithm:

- represent the pair `to -> from` as two numbers `A` and `B` (refer to the discussion until now how we can do that)
- use the Calkin-Wilf sequence (combined with the [continued fraction formula](https://en.wikipedia.org/wiki/Continued_fraction#Finite_continued_fractions)) to find the index of `A/B` 
- or conversely use the sequence to transform the index into the `A/B` fraction and then transform the numerator and denominator into the original sequences

This is just speculation but it should work in theory. Also, it is fairly complicated so perhaps there is a better way to do it by making some simplifying assumptions? (like us eliminating the lexicographic ordering requirement).

## Source code

A complete implementation of the above algorithms (with tests!) in Python 3 can be found [on GitHub](https://github.com/cdman/nth-element-of-dictionary/).

