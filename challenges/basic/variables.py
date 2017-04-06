"""
EXERCISES:
========================================================================================================================
Es.1
- Assign 3 variables (a, b, c) with float numbers. Figure out the sum, the product, the 
difference and the quotient of the variables putting each operation in a new var.

Es.2
- Assing 2 string vars (try the multiple assignment) one with "py" and one with "thon" than concatenate the strings and 
print the result.

Es.3
- Given a string '125343.43' in var 'a' convert it into float number, than multiply 'a' with b (b=12).
========================================================================================================================

Types
Python has many native datatypes. Here are the important ones:

    1) Booleans are either True or False.
    2) Numbers can be integers (1 and 2), floats (1.1 and 1.2), fractions (1/2 and 2/3), or even complex numbers.
    3) Strings are sequences of Unicode characters, e.g. an html document.
    4) Bytes and byte arrays, e.g. a jpeg image file.
    5) Lists are ordered sequences of values.
    6) Tuples are ordered, immutable sequences of values.
    7) Sets are unordered bags of values.
    8) Dictionaries are unordered bags of key-value pairs.

Var assignment
An assignment statement creates new variables and gives them values:

>>> message = 'And now for something completely different'
>>> n = 17
>>> pi = 3.1415926535897932

This example makes three assignments. The first assigns a string to a new variable named message; the second gives the 
integer 17 to n; the third assigns the (approximate) value of π to pi.

The type of a variable is the type of the value it refers to.
    
>>> type(message)
<class 'str'>
>>> type(n)
<class 'int'>
>>> type(pi)
<class 'float'>

Multiple assignment
The left and right side must have the same number of elements. For example, the following script has several examples 
of multiple assignment.

>>> x1,y1 = 2,3 # point one
>>> x2,y2 = 6,8 # point two
>>> m,b = float(y1-y2)/(x1-x2), y1-float(y1-y2)/(x1-x2)*x1
>>> print("y=",m,"*x+",b)
y= 1.25 *x+ 0.5

Reference: here a good reference to better understand types in python 3
https://www.digitalocean.com/community/tutorials/understanding-data-types-in-python-3

Tip:
If you have lines in the docstring (this string) that look like interactive
Python sessions, you can use the doctest module to run and test this code.

Try: python -m doctest -v variables.py

See: https://docs.python.org/3/library/doctest.html
"""
