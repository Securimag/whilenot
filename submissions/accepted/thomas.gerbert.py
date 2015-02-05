#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    +:  original (redefine del)
        no for
        no import

    -:  active loop

"""

#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.


class Loop:
    cpt = 0

    def __del__(self):
        Loop.cpt += 1
        print('Loop: %d' % Loop.cpt)
        Loop()

if __name__ == '__main__':
    Loop()
