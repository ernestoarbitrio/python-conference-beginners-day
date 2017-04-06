"""
EXERCISES:
========================================================================================================================
Es.1
- The word 'in' is a boolean operator that takes two strings and returns True if the first appears as a substring in 
the second: use this operator to check if 'an' or 'seed' is present in 'banana'.

Es.2
- There is a string method called count. Read the documentation of this method and write an invocation that counts the 
number of 'a' in 'banana'.

Es.2
- Using the replace method change all the 'a' in 'banana' with $ char.

Es.3
- Given the string 'How old are you?' transform it to obtain 'How old is she?', and then print only the 'old' word of 
the sentece using slicing.

Es.4
- Write a program that given a string displays the letters backward, one per line. 
Hint: use iteration statements
========================================================================================================================


STRINGS
A string is a sequence of characters. You can access the characters one at a time with the bracket operator:
>>> fruit = 'banana'
>>> letter = fruit[1]

The second statement selects character number 1 from fruit and assigns it to letter. The expression in brackets is 
called an index. The index indicates which character inthe sequence you want (hence the name). But you might not get 
what you expect:

>>> print(letter)
a

For most people, the first letter of 'banana' is b, not a. But for computer scientists, the index is an offset from 
the beginning of the string, and the offset of the first letter is zero.

>>> letter = fruit[0]
>>> print(letter)
b

So b is the 0th letter (“zero-eth”) of 'banana', a is the 1th letter (“one-eth”), and n is the 2th (“two-eth”) letter.
You can use any expression, including variables and operators, as an index, but the value of the index has to be an 
integer. Otherwise you get:

>>> letter = fruit[1.5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: string indices must be integers


String length
len is a built-in function that returns the number of characters in a string:
>>> fruit = 'banana'
>>> len(fruit)
6

Strings Are Immutable
It is tempting to use the [] operator on the left side of an assignment, with the intention of changing a character 
in a string.
For example:

>>> greeting = 'Hello, world!'
>>> greeting[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment


String Slices
A segment of a string is called a slice. Selecting a slice is similar to selecting a character:

>>> s = 'Monty Python'
>>> print(s[0:5])
Monty
>>> print(s[6:12])
Python

The operator [n:m] returns the part of the string from the “n-eth” character to the “m-eth” character, including the 
first but excluding the last.

String Methods
A method is similar to a function—it takes arguments and returns a value—but the syntax is different. For example, 
the method upper takes a string and returns a new string with all uppercase letters:
Instead of the function syntax upper(word), it uses the method syntax word.upper().

>>> word = 'banana'
>>> new_word = word.upper()
>>> print(new_word)
BANANA

This form of dot notation specifies the name of the method, upper, and the name of the string to apply the method to, 
word. The empty parentheses indicate that this method takes no argument.
A method call is called an invocation; in this case, we would say that we are invoking upper on the word.
As it turns out, there is a string method named find that is remarkably similar to the function we wrote:

>>> word = 'banana'
>>> index = word.find('a')
>>> print(index)
1

In this example, we invoke find on word and pass the letter we are looking for as a parameter. Actually, the find method
is more general than our function; it can find substrings, not just characters:

>>> word.find('na')
2


Tip:
If you have lines in the docstring (this string) that look like interactive Python sessions, you can use the doctest 
module to run and test this code.

Try: python -m doctest -v strings_operations.py

See: https://docs.python.org/3/library/doctest.html

Credit to Allen Downey and his excellent book Think Python, from which I stole some text.
"""

# Write your code here or in your interpreter console. Enjoy!!!
