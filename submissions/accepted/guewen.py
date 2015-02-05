#!/usr/bin/env python

"""
    +:  original
        no for

    -:  imports
        complex tools

"""

from collections import deque
from itertools import cycle

loop = cycle([1])
deque(loop, maxlen=1)
