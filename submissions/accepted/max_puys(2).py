#!/usr/bin/env python

"""
    +:  no for
        passive loop

    -:  same as previous submission (almost)

"""


import time
from threading import Timer


def toInfinityAndBeyond():
    Timer(1, toInfinityAndBeyond, ()).start()

if __name__ == "__main__":
    Timer(1, toInfinityAndBeyond, ()).start()
