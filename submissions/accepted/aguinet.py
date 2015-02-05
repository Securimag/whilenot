"""
    +:  no import

    -:  active loop
        for
        
"""


class InfiniteIter:
    def __iter__(self): return self
    def next(self):
        return 1

for i in InfiniteIter():
    pass
