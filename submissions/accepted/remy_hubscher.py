"""
    +:  simple
        no import
        no for

    -:  not original
        brutal
        active loop

"""


def toto():
    try:
        toto()
    except RuntimeError:
        toto()
            
toto()
