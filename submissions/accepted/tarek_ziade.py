
"""
    +:  original
        passive loop

    -:  not really infinite
        imports
        kinda brutal

"""


from time import sleep
import atexit
import signal

def do():
    print('yo')
    sleep(.1)
    atexit.register(do)

signal.signal(signal.SIGINT, lambda x, y: None)
signal.signal(signal.SIGTERM, lambda x, y: None)

do()
