##10demo.py by Dean Abdelnaby

print("hello world") #greeting

"""
holy moly
this is a
 multi-line comment
"""

import math #importing math module
a = 3 # side 1
b = 4 # side 2
c = math.sqrt(a**+2 + b**2) # pythag theorem
print(c) 

print(type(a), type(b), type(c), sep=',', end='!\n')

## functions

def pythagoras(a,b):
    return math.sqrt(a**2 + b**2)
    

hyp = pythagoras(3, 4)
print(hyp)
