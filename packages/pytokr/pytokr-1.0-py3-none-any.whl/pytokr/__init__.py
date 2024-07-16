"""
Author: Jose Luis Balcazar, ORCID 0000-0003-4248-4528, balqui at GitHub
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)
Project start date: Germinal 2022.

This source: version 1.0
This source date: late Messidor, 2024

Very simple tokenizer for `stdin` and similar objects. Finds items
(simply white-space-separated tokens) in a string-based iterable
such as `stdin` (default). Ends of line are counted as white space 
but are otherwise ignored. 

Provides a function `pytokr()` that returns: 
- a function (often called `item()`) that obtains the next item and 
- if required, an iterator (often called `items()`) on which one can 
  run a `for` loop to traverse all the items.
Of course, the returned values of `pytokr()` may get whatever names the 
user want; alternatively, the user may import directly `item()` and 
`items()`.

Both combine naturally: the individual item function can be called 
inside the for loop of the iterator and this advances the items; 
so, the next item at the loop will be the current one after the 
local advances.

Token items are returned as strings; the user should cast them as
int or float or whatever when appropriate.

Programmed using a lexical closure strategy.

Usage: 
(a) simply import `item`, `items`, or both as necessary, maybe 
renaming them if you wish in the standard Python way (using an
`as` clause), or 
(b) import `pytokr` to obtain a function that, when called, will
return a function operating as `item()`; to obtain additionally an 
iterator, call `pytokr(iter = True)` and grab also the second outcome; 
for usage on another string-based iterable, give that iterable as first, 
unnamed argument of the call to `pytokr()`.

See examples below.

In former versions 0.*, importing item and/or items alternated
a deprecation status. Finally it was decided to keep them available.
Conversely, in very early versions, the name `make_tokr` was employed 
but, once deprecated, has never been undeprecated again. Usage is 
still possible for backwards compatibility but a deprecation warning 
will be sent through stderr.
"""

__version__ = "1.0"

def detect_end_of_data(next_method):
    "Renaming the exception so as to hide the StopIteration message from the novice users"
    EndOfDataError = Exception("Function produced by pytokr called at end of data, nothing to read")
    ok = True
    def new_next():
        try:
            return next_method()
        except StopIteration:
            ok = False
        if not ok:
            raise EndOfDataError
    return new_next

def pytokr(f = None, /, iter = False):
    '''
    make iterator and next functions out of iterable of split strings
    return next function and, if requested, iterator too
    '''

    from itertools import chain

    def the_it():
        "so that both outcomes are called with parentheses"
        return it

    if f is None:
        from sys import stdin as f
    it = chain.from_iterable(map(str.split, f))
    new_next = detect_end_of_data(it.__next__)
    if iter:
        return new_next, the_it
    return new_next

item, items = pytokr(iter = True)



# Everything below, down to "if __name__ ...", is unnecessary and
# kept only for partial backwards compatibility: all the functions 
# work, but will print a deprecation warning through stderr.

def make_tokr(f = None):
    '''
    make iterator and next functions out of iterable of split strings
    Deprecated - import pytokr instead, see https://github.com/balqui/pytokr
    Looks complicated because of inheriting from the deprecation / undeprecation phases
    Slated to be removed in the next version
    '''
    from sys import stderr # for deprecation warning

    from itertools import chain
    
    print("[stderr] Since version 0.1.*, function make_tokr is deprecated;",
          file = stderr, end = " ")
    print("please see https://github.com/balqui/pytokr", file = stderr)

    def the_it():
        def depr_it():
            return it
        return depr_it()

    def the_it_next():
        '''
        so that both, items and item, are called with parentheses
        '''
        def depr_it():
            return it.__next__()
        return detect_end_of_data(depr_it)

    if f is None:
        from sys import stdin as f
    it = chain.from_iterable(map(str.split, f))
    return the_it, the_it_next()

if __name__ == "__main__":
    "example usages"
    print("Test of imported item, items.")
    print("Please write some lines and end with a line containing only control-D:")
    print("First word of first line was:", item()) 
    print("Then comes the rest of the lines.")
    for w in items():
        "traverse rest of stdin"
        print(w)
    print("Test of read/loop from imported pytokr.")
    read, loop = pytokr(iter = True)
    print("Please write some lines and end with a line containing only control-D:")
    print("First word of first line was:", read()) 
    print("Then comes the rest of the lines.")
    for w in loop():
        "traverse rest of stdin"
        print(w)
    print("\n\nNow with another iterable made of splittable strings,")
    g = [ "10 11 12", "13 14", "15 16 17 18" ]
    print("namely:", g)
    item, items = pytokr(g, iter = True) # traverse g instead of stdin
    for w in items():
        "see how we can mix them up"
        print("\nCurrent value of w at for w in items() loop:", w)
        print("item() grabbed within the loop:", item())
        print("another item() grabbed also within the loop:", item())
