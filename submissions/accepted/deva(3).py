
"""
    +:  no for
        no import

    -:  kinda brutal

"""

def f():
    try:
        reduce(lambda x, y: f(), xrange(3))
    except:
        pass
    return 0
f()
