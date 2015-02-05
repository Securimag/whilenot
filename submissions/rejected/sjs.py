
"""
    REJECTED: Stack overflow due to list growing 

"""

def endless_todos():
    todos = ['faire la vaiselle']

    for i in todos:
        print 'Et maintenant: %s !' % i
        todos.append(i)
