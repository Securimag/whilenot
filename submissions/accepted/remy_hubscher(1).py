
"""
    +:  no for (hidden in map)
        simple
        passive loop

    -:  idea to use iter not original
        import

"""

from time import sleep

map(lambda x: sleep(1000), iter(str, 1))
