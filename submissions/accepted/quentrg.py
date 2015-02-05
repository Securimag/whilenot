
"""
    +:  no for
        passive loop (hm)

    -:  not original

"""


import time

class Loop(object):
    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        time.sleep(0.0001)
        return None

if __name__ == "__main__":
    any(Loop())
