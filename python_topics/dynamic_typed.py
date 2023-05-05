# Dynamic typing means that the type of the variable 
# is determinated only during runtime

import cython

n = 5 # object, all in python are objects
dir(n) # This function returns all properties and methods of the specified object

# Cython, allows one to add statictyping information. Python + C

'''
    Dynamic vs Static

    Dynamic typing: This means that the Python interpreter does type checking only as code runs.
    The type of a variable is allowed to change over its lifetime.
    
    Static typing: Static type checks are performed without running the program.
    You can found it in C and Java.
    To implement this you can use Cython -> cdef cpdef

'''

if False:
    1 + "two" # This line never runs
else:
    print(1 + 2)

variable =  "Hello"
print(type(variable))

variable = 90.0
print(type(variable))
