
"""
    +:  no for
        no import
        smart

    -:  already seen

"""

class I(object):
    def __next__(self):
        return 1
    def __iter__(self):
        return self
sum(I())
