
"""
    +:  no for
        simple

    -:  import
        active loop
        idea not original (reduce and iter)

"""

# Explication:
# iter() a un comportement particulier quand on lui passe deux arguments. Il itère sur le premier argument en l’appelant tant que la valeur du second argument n’est pas trouvée. int() retournant 0 on voit donc que iter(int, 1) nous produit un itérateur sans fin.
# 
# Le reduce va jouer le rôle de la boucle infinie puisqu’il itèrera sur un ensemble infini. Le lambda donne simplement l'impression de faire quelque chose ;)
# 
# L’ensemble se basant sur des itérateurs plutôt que sur des listes, la consommation mémoire restera stable dans le temps. Vu que le résultat du lambda sera 0, on ne risque pas non plus de dépasser la limite d’un entier.

import functools
functools.reduce(lambda a, b: a*b, iter(int, 1))
