# Python defines built-in data structures, removing the work from the operator

# math library
import math
math.factorial(100) # method 'factorial"
# methods are functions

# help(math)
# dir(math)
# dir(), allows you to view the current namespace in 

# import modules from "math" library and rename as "fac"
from math import factorial as fac
n = 100
fac(n)

# Two types of loops: 1- while, 2 - for

# expr=True, execute block, once defined it will be true
expr = 1
while expr: # expr is converted to "bool" as is if by the bool() constructor
    print("Loop while expr is True")

# COLLECTIONS types

str # are immutable, once assigned it will be stored in memory with that id point-in-time

# \n, for escapte sequences look it up in python.org

# when using back slashes for "escape characters" use the raw strings
# prefix 'r' followed by the string
path = r"C:\Users\Merlin\Documnets\Spell"
path

# Bytes strings are prefixed by lower 'b'
something = "some jiberish that you do not care about"
data = something.encode('utf-8')

# bytes string conversion ?????
# can we use data printed from Ansible to convert to bytes strings
# This is the problem we have from configuration templates

# For-Loops
# take items one-by-one from an iterable object, binding a name to the current item
iterable = 'something_to_be_iterable'
for item in iterable:
    body

cities = ['Hanford', 'Los Angelos', 'Cameron', 'London']
for city in cities: # requires a placeholder variable to run the task
    print(city)

colors = {'crimson': 0x56b8, 'green': 0x445f}
for color in colors:
    print(color, colors[color])

########################################################################
# snippet from plurasight
from urllib.request import urlopen

with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

for word in story_words:
    print(word)

########################################################################

## functions
def square(x):
    return x * x

square(5)

def even_or_odd(n):
    if n % 2 == 0:
        print('even')
        return
    print('odd')

even_or_odd(3)

####################
from urllib.request import urlopen

def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    
    for word in story_words:
        print(word)


###### WEB DEVELOPMENT "serivce.py"

from flask import Flask

# create an instance of flash and assigning it to the app variable
app = Flask(__name__)

@app.route("/") # route declaration
def hello():
    return "Hello World"

### in terminal
FLASK_APP=service.py flask run
# http request
curl localhost:5000

##### reloading python files when modified
import importlib
importlib.reload(hello_world) # within the arguements reload modifief file

# py <3.4
import imp
import.reload(filename)

# py 2.0
reload(filename)

###### 25 JAN 22020, "Modularity"

from urllib.request import urlopen

def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words

def print_words(story_words):
    for word in story_words:
        print(word)

def main():
    words = fetch_words()
    print_words(words)

if __name__ == '__main__':
    main()

########################################

from words import (fetch_words, print_words)
print_words(fetch_words())

from words import * # imports everything from a module

################### Documentation ###########################
"""Retrive and print words from a URL. (module docstrings should be placed in beging of module)

Usage:
    python3.6 words.py <URL>
    python3.6 words.py http://sixty-north.com/c/t.txt
"""


import sys
from urllib.request import urlopen

def fetch_words(url):
    """ Fetch a list of words from a URL.
    Args:
        url: The URL of a UTF-8 text document.

    Returns"
        A list of stings
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words
# two line breaks betwen functions, PEP8

def print_items(items):
    for item in items:
        print(item)


def main(url):
    """ need to accept as a command line arguement,
    have to the 'sys.argv[]' attribute. Must 'import sys' module """
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main(sys.argv[1]) # The 0th arg is the module filename

"""
from words import * < this will import individual functions from 
module and will allow to access individually.

when using the docstring, you can call the docstring information
with "help(fetch_words)" and it will print that functions respective
docstring

# Just in case you need to reload a module
import importlib
importlib.reload(module)

"""

chmod +x words.py # make file executable
./words.py http://sixty-north.com/c/t.txt # execute
"""
Summary:
Modules can be executed directly with
    python module_name.py

Brought into REPL or other moduels with
    import module_name

Named functions defined with the def keyword:
   def function_name(arg1, argn)

Return from functions usting "return" at end of function

Use __name__ to determine how the module is being used

If __name__ == "__main__" the module is being executed

Command line arguments are accessible through sys.argv

The script filename is in sys.argv[0]

Docstrings provide help() in REPL

"""

############ "OBJECTS" module

>>> a = 1
>>> b = 4
>>>
>>>
>>> a is b
False
>>> a = b
>>> a is b
True

Python has nameed references to objects, references behave more like labels which allow us to retrieve objects

Value VS Identity

Value - equivalent "contents" (==)
Identity - same object refernce (is)

Value comparison can be controlled programatically

>>> c = [4, 3, 1]
>>> d = [4, 3, 1]
>>> id(c)
140559721832520
>>> id(d)
140559721834568
>>> c == d # contents
True
>>> c is d # refernced object
False

# The garbage collector reclaims unreachable objects, objects with no tag/label

>>> m = [9, 15, 24]
>>> def modify(k):
...     k.append(39)
...     print("k =", k)
...
>>> modify(m)
k = [9, 15, 24, 39]
>>> m
[9, 15, 24, 39]
>>>
>>> f = [14, 23, 37]
>>> def replace(g):
...     g = [17, 28, 45]
...     print("g =", g)
...
>>> replace(f)
g = [17, 28, 45]
>>> f
[14, 23, 37]
>>> g
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'g' is not defined



>>> def banner(message, border='-'):
...     line = border * len(message)
...     print(line)
...     print(message)
...     print(line)
...
>>> banner("Victor Morquecho") # this uses the default value '-'
----------------
Victor Morquecho
----------------
>>> banner("Victor Morquecho can do some Python")
-----------------------------------
Victor Morquecho can do some Python
-----------------------------------

>>> banner("Sun, Moon and Stars", "*") # or you can specify another value
*******************
Sun, Moon and Stars
*******************

>>> banner("Sun, Moon and Stars", border="*")
*******************
Sun, Moon and Stars
*******************
# keyword arguments can be specified in any order
>>> banner(border=".", message="Hello from Earth")
................
Hello from Earth
................
>>>

banner("Positional arg", "keyword arg")

>>> def add_spam(menu=[]):
...     menu.append("spam")
...     return menu
...
>>> breakfast = ["bacon", "eggs"]
>>> add_spam(breakfast)
['bacon', 'eggs', 'spam']
>>>
>>> def add_steak():
...     menu = []
...     menu.append("steak")
...     return menu
...
>>> breakfast
['bacon', 'eggs', 'spam']
>>>
>>> add_steak(breakfast)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add_steak() takes 0 positional arguments but 1 was given


>>> def add_steak(menu=None):
...     if menu is None:
...         menu = []
...     menu.append("spam")
...     return menu
...
>>> add_steak()
['spam']
>>>


Python is a dynamic type system, object types are only resolved at runtime

Python Name Scopes:
Local
Enclosing
Global
Built-in

>>> import words
>>>
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'add_spam', 'add_steak', 'b', 'banner', 'breakfast', 'c', 'd', 'f', 'm', 'modify', 'replace', 'words']
>>>
>>> dir(words)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fetch_words', 'main', 'print_items', 'sys', 'urlopen']
>>> dir(words.fetch_words)
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> dir(words.fetch_words.__doc__)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index',
'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(words.fetch_words.__doc__)
No Python documentation found for 'Fetch a list of words from a URL.\n    Args:\n        url: The URL of a UTF-8 text document.\n\n    Returns"\n        A list of stings'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.
