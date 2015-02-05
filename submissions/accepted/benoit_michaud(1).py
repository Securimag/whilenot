
"""
    +:  smart
        passive loop
        no for

    -:  not really infinite loop
    
"""


import time

def test():
    time.sleep(24*60*60)
    print('je suis pas mort')
    test()
test()
