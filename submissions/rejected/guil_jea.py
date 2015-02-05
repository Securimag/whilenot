#!/usr/bin/python

"""
    +:  no for
        passive loop

    -:  imports

    REJECTED: do not loop forever

"""

from threading import Thread
import time

class Not_while(Thread):
    def run(self):
        thread_X = Not_while()
        thread_X.start()

thread_1 = Not_while()
thread_1.start()
thread_1.join()
