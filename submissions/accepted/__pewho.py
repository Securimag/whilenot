#!/usr/bin/env python3

"""
    +:  no for
        original
        elegant

    -:  import

"""


from subprocess import Popen
import sys
from os import path

__author__ = 'pewho'

"""
	While Not Challenge 
	===================

	Solution basée sur subprocess, pas de for :)

	Lancement 
	>>> python3 subprocess_program.p
"""

if __name__ == '__main__':
	try:
		i = int(sys.argv[1])
	except IndexError:
		i = 0

	print('PING {}'.format(i) if i % 2 == 0 else 'PONG {}'.format(i))

	Popen(['python', path.abspath(__file__), str(i+1)])
