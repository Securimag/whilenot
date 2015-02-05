
"""
    +:  passive loop
        simple

    -:  not original
        for
        import

"""

# just for not having a CPU at 100%
from time import sleep
sleep_time = 0.00001  # 0.01 ms

depth = 99999999

def fn():
    sleep(sleep_time)
    for _ in range(depth):
        try:
            fn()
        except RuntimeError:  # stack overflow, avoid the crash
            pass

# yeah, if __main__ == 'iDontRememberAndIAmToLazyToGoogleIt' would be better ...
fn()
