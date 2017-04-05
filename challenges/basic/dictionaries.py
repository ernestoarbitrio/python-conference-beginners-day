"""
EXERCISES
========================================================================================================================
Es.1
- Given the following dictionary:
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
Try to do the followings:
1) Add a key to inventory called 'pocket'.
2) Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
3) .sort() the items in the list stored under the 'backpack' key.
4) Then .remove('dagger') from the list of items stored under the 'backpack' key.
5) Add 50 to the number stored under the 'gold' key.

Es.2
- Create 2 new dictionaries called 'prices' and 'stock' using {} format with this values:
    --prices--
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3

    --stock--
    "banana": 6,
    "apple": 7,
    "orange": 1,
    "pear": 3

2) Loop through each key in prices. For each key, print out the key along with its price and stock information. 
   Print the answer in the following format:
        apple
        price: 2
        stock: 0

3) Let's determine how much money you would make if you sold all of your food:
    - Create a variable called total and set it to zero.
    - Loop through the prices dictionaries. For each key in prices, multiply the number in prices by the number in 
      stock. Print that value into the console and then add it to total.
    - Finally, outside your loop, print total.
========================================================================================================================


Dictionaries

A dictionary is like a list, but more general. In a list, the indices have to be integers; in a dictionary they can be 
(almost) any type. You can think of a dictionary as a mapping between a set of indices (which are called keys) and a set
of values. Each key maps to a value. The association of a key and a value is called a key-value pair or sometimes an 
item.
As an example, we’ll build a dictionary that maps from English to Spanish words, so the keys and the values are all 
strings.
The function dict creates a new dictionary with no items. Because dict is the name of a built-in function, you should 
avoid using it as a variable name.

>>> eng2sp = dict()
>>> print(eng2sp)
{}

The squiggly-brackets, {}, represent an empty dictionary. To add items to the dictionary, you can use square brackets:

>>> eng2sp['one'] = 'uno'

This line creates an item that maps from the key ’one’ to the value 'uno'. If we print the dictionary again, we see a 
key-value pair with a colon between the key and value:

>>> print(eng2sp)
{'one': 'uno'}

This output format is also an input format. For example, you can create a new dictionary with three items:

>>> eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'} 

But if you print eng2sp, you might be surprised:

print(eng2sp)
{'one': 'uno', 'three': 'tres', 'two': 'dos'}

The order of the key-value pairs is not the same. In fact, if you type the same example on your computer, you might get
a different result. In general, the order of items in a dictionary is unpredictable.

But that’s not a problem because the elements of a dictionary are never indexed with integer indices. Instead, you use 
the keys to look up the corresponding values:

>>> print(eng2sp['two'])
dos

The key ’two’ always maps to the value 'dos' so the order of the items doesn’t matter. If the key isn’t in the 
dictionary, you get an exception:

>>> print(eng2sp['four'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'four'


Tip:
If you have lines in the docstring (this string) that look like interactive Python sessions, you can use the doctest 
module to run and test this code.

Try: python -m doctest -v string_operations.py

See: https://docs.python.org/3/library/doctest.html

Credit to Allen Downey and his excellent book Think Python, from which I stole some text.
"""