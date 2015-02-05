#! /usr/bin/env python

"""
        +:  elegant code
            well presented
            well explained
            no for
            
        -:  use of itertools not original
            pipe waiting is kinda cheated (yet clever)
    
"""



"""
Usage:
    ./infinity.py [cmd]

Launch an infinite program using cmd.
No for or while are used to implement any of them.

"""

import os
import sys
import time
import itertools

# Running *forever* means we might not be building any list element, as they
# would tend to overcome our memory at some point, even if we have a huge
# amount of it.


def infinite(x):
    def fct(x):
        # Called each loop
        sys.stdout.write('.')
        sys.stdout.flush()
        # sleep, so we don't overflow our screen too fast :)
        time.sleep(.1)
        return x
    if hasattr(itertools, 'imap'):
        # python2, map tries to build a list
        return itertools.imap(fct, itertools.repeat(x))
    # python3, map returns an iterator
    return map(fct, itertools.repeat(x))


def _pipe():
    # Open a pipe, and wait in infinite i/o on it
    # Note: Not a loop. It will *NOT* use any CPU while hanging.
    pin, pout = os.pipe()
    os.fdopen(pin).read()


def _pipe_data():
    # Loops infinitely the data within a pipe
    import shutil
    pin, pout = os.pipe()
    fin = os.fdopen(pin)
    fout = os.fdopen(pout, 'w', 0)  # 0 = unbuffered
    data = 'data\n'
    fout.write(data)
    shutil.copyfileobj(fin, fout, len(data))  # len() as chunk sizes


_funcs = {
    'any': {
        'help': "uses `any()' to loop",
        'fct': lambda: any(itertools.repeat(0)),
    },
    'all': {
        'help': "uses `all()' to loop",
        # cycle instead of repeat
        'fct': lambda: all(itertools.cycle([1])),
    },
    # sum zeros, or it might get storing the int might overflow the memory
    'sum': {
        'help': "uses `sum()' to loop",
        'fct': lambda: sum(itertools.repeat(0)),
    },
    'pipe': {
        'help': "blocks on reading within a pipe",
        'fct': _pipe,
    },
    'pipe-data': {
        'help': "read/write data along a single pipe",
        'fct': _pipe_data,
    },
    'sum-print': {
        'help': "like `sum' and `map' iterator to actualy do some work too",
        'fct': lambda: sum(infinite(0)),
    },
    'writelines': {
        'help': "Write infinite lines",
        'fct': lambda: sys.stdout.writelines(
                            itertools.repeat("To infinity and beyond\n"))
    },
}


def _usage():
    print(__doc__)
    print("Valid commands:")
    for cmd in sorted(_funcs):
        print("  {0:16}{1}".format(cmd, _funcs[cmd]['help']))
    print("")
    sys.exit(0)

if len(sys.argv) == 2 and sys.argv[1] in _funcs:
    _funcs[sys.argv[1]]['fct']()
    print("Hey, what am I doing here?")
    print("Something must have gone wrong!")
    sys.exit(1)

_usage()
