
"""
    +:  no for
        passive loop
        smart

    -:  import
        seen several times

"""

import threading
l=threading.Lock()
l.acquire()
l.acquire()
