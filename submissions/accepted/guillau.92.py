
"""
    +:  no for
        passive loop
        smart

    -:  import
        seen several times

"""

import threading
lock = threading.Lock()
lock.acquire()
lock.acquire()
