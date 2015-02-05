#!/usr/bin/env python

"""
    Several propositions in one file, so each one has been 
    considered independantly from the others.
    
    WINNER: opt #2
        file = open('/dev/random')
        file.read()
    
"""


import sys
import signal
import os

if len(sys.argv) != 2:
    print "Usage : python while_not.py <1-9>"
    exit(1)

opt = int(sys.argv[1])

if opt == 1:
    """
        REFUSED: stack overflow at some point
        
    """
    # On modifie l'iterateur a la volee, facile
    # Hum, la memoire augmente.
    tab = [1]
    for i in tab:
        tab.append(1)
elif opt == 2:
    """
        +:  no for
            no import
            simple
            original
            elegant
            
        -:  active loop
            os-dependant
        
    """
    # pas de module, que des fonctions builtin, c'est bon non ? :D
    file = open('/dev/random')
    file.read()
elif opt == 3:
    """
        +:  no import
            no for
            simple

        -:  not really a loop ...

    """
    # ca ne s'arrete pas tant qu'on n'entre pas d'EOF... Ca rentre dans les
    # conditions ?
    input()
elif opt == 4:
    """
        +:  no for
            no import

        -:  not original
            brutal

    """
    # Si on ecrase le handler de l'exception de recursivite max atteinte, ca
    # ne s'arretera plus...
    # Attention, ne catche plus ^C
    def fail():
        try:
            fail()
        except:
            fail()
    fail()
elif opt == 5:
    """
        REFUSED: Stack overflow at some point

    """
    # Bon OK, c'est la meme que la 1 avec le for camoufle dans le filter().
    # ca marche aussi avec map()
    tab = [1]
    print filter(lambda x: tab.append(1), tab)
elif opt == 6:
    """
        +:  no for
            no import
            simple

        -:  already seen
            kinda cheated (no loop)

    """
    # Techniquement, il n'y a pas de boucle vu que le process est endormi.
    signal.pause()
elif opt == 7:
    """
        +:  smart
            no import
            no for

        -:  already seen

    """
    # detruire l'objet en cree un nouveau, etc etc
    # On abuse du ramasse-miettes
    # Hum, zut, la memoire augmente.
    # genere une erreur si on n'importe pas os, je ne sais pas pourquoi.
    class Yolo:
        def __del__(self):
            hihi = Yolo()
    hihi = Yolo()
elif opt == 8:
    """
        +:  no import

        -:  not original

    """
    # iterateur infini
    class Iterator_fail:
        def next(self):
            return False
        def __iter__(self):
            return self
    foo = Iterator_fail()
    for i in foo:
        pass
elif opt == 9:
    """
        +:  no for
            no import
            smart

        -:  already seen

    """
    # Un peu plus subtil : le meme, sans for
    class Iterator_fail:
        def next(self):
            return False
        def __iter__(self):
            return self
    foo = Iterator_fail()
    any(foo)
elif opt == 10:
    """
        +:  no for
            clever

        -:  import

    """
    # Solution 7 corrigee au niveau memoire qui augmente
    # Un appel explicite au garbage collector corrige le probleme
    # Le module gc est-il accepte ? Le garbage collector est appele dans tous
    # les cas de toute facon...
    import gc
    class Yolo:
        def __del__(self):
            hihi = Yolo()
            gc.collect()
    hihi = Yolo()
