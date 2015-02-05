
"""
    +:  no for
        smart
        obfuscated
        
    -:  already seen
        import
    
"""

import dis
def func():
    print("lol")
    return a

fco = func.__code__
func_code = list(fco.co_code)
func_code = [ 113, 0, 0 ]

func.__code__ = type(fco)(
        fco.co_argcount,
        fco.co_kwonlyargcount,
        fco.co_nlocals,
        fco.co_stacksize,
        fco.co_flags,
        bytes(func_code),
        fco.co_consts,
        fco.co_names,
        fco.co_varnames,
        fco.co_filename,
        fco.co_name,
        fco.co_firstlineno,
        fco.co_lnotab,
        fco.co_freevars,
        fco.co_cellvars
)
print(list(func.__code__.co_code))
dis.dis(func)
func()





