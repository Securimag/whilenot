
"""

    +:  passive loop
        no for
        
    -:  not litterally infinite
        mem usage growing 
        import

"""

import time

sleepTime = 1000000

def sleepRec(n):
    print(n)
    time.sleep(sleepTime)
    sleepRec(n+1)
                
sleepRec(0)

