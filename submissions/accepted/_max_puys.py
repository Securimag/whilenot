#!/usr/bin/env python

"""
    +:  original
        first submission without for
        passive loop

    -: import

"""

import sched, time

def toInfinityAndBeyond():
    s.enter(1, 1, toInfinityAndBeyond, ())
    s.run()

if __name__ == "__main__":
    s = sched.scheduler(time.time, time.sleep)
    s.enter(1, 1, toInfinityAndBeyond, ())
    s.run()
