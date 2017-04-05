"""
EXERCISES:
========================================================================================================================
Es.1
- Write a Python function to find the Max of three numbers.

Es.2
- Write a Python function to sum all the numbers in a given list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20

Es.2
- Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output : 
No. of Upper case characters : 3
No. of Lower case Characters : 12

Es.3
- Write a function named right_justify that takes a string named s as a parameter and prints the string with enough l
eading spaces so that the last letter of the string is in column 70 of the display.
    [] right_justify('allen')
    []                                                                 allen

Es.4
- Write a Python function to check whether a number is perfect or not.
According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper
positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot 
sum). Equivalently, a perfect number is a number that is half the sum of all of its positive divisors 
(including itself).
Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. 
Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 
The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.

========================================================================================================================


FUNCTIONS
When you define a function, you specify the name and the sequence of statements. Later, you can “call” the function 
by name. We have already seen one example of a function call:

>>> type(32)
<class 'int'>

The name of the function is type. The expression in parentheses is called the argument of the function. The result, 
for this function, is the type of the argument. It is common to say that a function “takes” an argument and “returns” 
a result. The result is called the return value.

WRITE FUNCTIONS
A function definition specifies the name of a new function and the sequence of statements that execute when the function
is called.

Here is an example:

>>> def print_lyrics():
...     print("I'm a lumberjack, and I'm okay.")
...     print("I sleep all night and I work all day.")
...

The value of print_lyrics is a function object, which has type 'function'. The syntax for calling the new function is 
the same as for built-in functions:

>>> print_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.

Parameters and Arguments
Some of the built-in functions we have seen require arguments. For example, when you call math.sin you pass a number as
an argument. Some functions take more than one argument: math.pow takes two, the base and the exponent.
Inside the function, the arguments are assigned to variables called parameters. Here is an example of a user-defined 
function that takes an argument:

>>> def print_twice(a, b): 
...     print(a)
...     print(b)
...     c = a + b
...     print(c)
...

Note taht when you create a variable inside a function (see example above), it is local, which means that it only exists
inside the function.


Tip:
If you have lines in the docstring (this string) that look like interactive Python sessions, you can use the doctest 
module to run and test this code.

Try: python -m doctest -v functions.py

See: https://docs.python.org/3/library/doctest.html

Credit to Allen Downey and his excellent book Think Python, from which I stole some text.
"""

# Write your code here or in your interpreter console. Enjoy!!!
