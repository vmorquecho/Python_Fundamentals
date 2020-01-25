#!/usr/bin/env python3.6
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
    """Print items on per line.
    
    Args:
        An iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """ need to accept as a command line arguement,
    have to the 'sys.argv[]' attribute. Must 'import sys' module """
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main(sys.argv[1]) # The 0

""" python3.6 words.py http://sixty-north.com/c/t.txt """
