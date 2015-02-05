
"""
    +:  no for
        smart

    -:  seen several times
        imports

"""

# Tested on Python 2.7.6 (default, Nov 10 2013, 19:24:18) [MSC v.1500 32 bit (Intel)] / Win x86
# @0vercl0k
import types
import opcode
def x():
    pass

c = x.func_code
x.func_code = types.CodeType( 
    c.co_argcount, c.co_nlocals, c.co_stacksize, c.co_flags, 
    ''.join(map(chr, [opcode.opmap['JUMP_ABSOLUTE'], 0, 0])), 
    c.co_consts, c.co_names, c.co_varnames, c.co_filename, 
    c.co_name, c.co_firstlineno, c.co_lnotab 
)
x()
