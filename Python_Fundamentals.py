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
    
    for word in story_words:
        print(word)
