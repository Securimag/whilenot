#!/usr/bin/python

"""
    +:  original 
        smart
        no import
        no for

    -:  idea already seen (too bad !)

"""

def f():
    pass

c = compile("def f(): pass", "noname", "exec")

type(f)(type(compile("def f(): pass", "noname", "exec"))(c.co_argcount, c.co_nlocals, c.co_stacksize,
c.co_flags, "780d00740000720f007103007103005764000053".decode('hex'), c.co_consts, c.co_names,
c.co_varnames, c.co_filename, c.co_name,
c.co_firstlineno, c.co_lnotab, c.co_freevars,
c.co_cellvars), globals(), "f", None, None)()
