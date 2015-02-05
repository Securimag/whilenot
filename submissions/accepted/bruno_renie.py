
"""
    +:  no for
        simple

    -:  not original
        imports

"""

import operator

from functools import reduce
from itertools import cycle


def run_forever():
    return reduce(operator.add, cycle([0]), 0)


if __name__ == '__main__':
    run_forever()
