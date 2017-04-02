"""
EXERCISES:

- Given a message and the number of times they want that message displayed,
write a program that print the message (with the iteration number by side) that number of times. 
Write it with forloop and with a whileloop.
Hint: read the enumerate built-in function in python3 docs.

- Write a program that will calculate the average (mean) of a set of numbers. 
This time, the user is to be asked how many numbers are to be averaged, 
they must then enter this number of numbers. Your program will calculate 
and display the average of those numbers.


There are two types of loop in Python:
    - the for loop 
    - the while loop

This simple for loop example would write "hello world" 5 times:

>>> for counter in range(5):
...     print("hello world")
hello world
hello world
hello world
hello world
hello world

This simple while loop example would write "hello world" 5 times:

>>> i = 0
>>> while (i<5):
...     print("hello world")
...     i +=1
hello world
hello world
hello world
hello world
hello world

The for loop is used to repeat a series of statements a given number of times. 
The first line of the for statement is used to state how many times the code 
should be repeated. A stepper variable is used to count 
through each iteration of the loop.


The range function
The range() function is one of Python's built in functions. It is is used 
to indicate how many times the loop will be repeated.

The structure of the range function is range(start, upto, step) in 
which the arguments of range are used as follows:

    - start and step are both optional.
    - upto must always be there, it means "up to but not including" the value.
    - start, upto, and step must all be integers

Examples: of the use of range:
    - range(10) produces the list: [0,1,2,3,4,5,6,7,8,9]
    - range1, 7) produces the list: [1,2,3,4,5,6]
    - range(0, 30, 5) produces the list: [0,5,10,15,20,25]
    - range(5, -1, -1) produces the list: [5,4,3,2,1,0]


Tip:
If you have lines in the docstring (this string) that look like interactive
Python sessions, you can use the doctest module to run and test this code.

Try: python -m doctest -v loop_range.py

See: https://docs.python.org/3/library/doctest.html

Credit to Allen Downey and his excellent book Think Python, from which
I stole this exercise.
"""

# Write your code here or in your interpreter console. Enjoy!!!
