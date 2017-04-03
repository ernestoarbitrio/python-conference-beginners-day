"""
EXERCISES:
========================================================================================================================
Es.1
- From the list ['physics', 'chemistry', 'math', 'Science', 2006, 1999, 1997, 2000], remove the last two elements, 
than capitalize all the string elements of the list.

Es.2
- Write a program to get the largest number from a list.

Es.3
- Write a Python program to count the number of strings where the string length is 2 or more and the first and last 
character are same from a given list of strings. 
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2

Es.4
- Given a list of numbers print the cumulative sum; that is, a new list where the ith 
element is the sum of the first i+1 elements from the original list. For example, the cumulative sum of [1, 2, 3] 
is [1, 3, 6]. Hint: .append method on a list add an element in it.
========================================================================================================================

Like a string, a list is a sequence of values. In a string, the values are characters; in a list, they can be any type. 
The values in a list are called elements or sometimes items.

There are several ways to create a new list; the simplest is to enclose the elements in square brackets ([ and ]):
    [10, 20, 30, 40]
    ['crunchy frog', 'ram bladder', 'lark vomit']

The first example is a list of four integers. The second is a list of three strings. The elements of a list don’t have 
to be the same type. The following list contains a string, a float, an integer, and (lo!) another list:
['spam', 2.0, 5, [10, 20]]

A list within another list is nested.

A list that contains no elements is called an empty list; you can create one with empty brackets, [].

As you might expect, you can assign list values to variables:

>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> numbers = [17, 123]
>>> empty = []
>>> print(cheeses, numbers, empty)
['Cheddar', 'Edam', 'Gouda'] [17, 123] []

List Slices
The slice operator also works on lists:

>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3]
['b', 'c']
>>> t[:4]
['a', 'b', 'c', 'd']
>>> t[3:]
['d', 'e', 'f']

If you omit the first index, the slice starts at the beginning. If you omit the second, the slice goes to the end. So 
if you omit both, the slice is a copy of the whole list.
>>> t[:]
['a', 'b', 'c', 'd', 'e', 'f']

Since lists are mutable, it is often useful to make a copy before performing operations that fold, spindle or mutilate 
lists. A slice operator on the left side of an assignment can update multiple elements:

>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3] = ['x', 'y']
>>> print(t)
['a', 'x', 'y', 'd', 'e', 'f']

Tip:
If you have lines in the docstring (this string) that look like interactive Python sessions, you can use the doctest 
module to run and test this code.

Try: python -m doctest -v lists.py

See: https://docs.python.org/3/library/doctest.html

Credit to Allen Downey and his excellent book Think Python, from which I stole some text.
"""

# Write your code here or in your interpreter console. Enjoy!!!
