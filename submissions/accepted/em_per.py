
"""
    +:  no import

    -:  not original
        use of for
        active loop

"""

class InfiniteLoop:
    def __init__(self):
        return
    def __iter__(self):
        return self
    def next(self):
        return 0

for i in InfiniteLoop():
    print i
