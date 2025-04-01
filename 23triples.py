# Title: 23 Triples
# Author: Dean A

import math

def pythagoras(n):
    x = int(n)
    for a in range(1,x):
        for b in range(a,x):
            c = math.sqrt(a**2 + b**2)
            if c % 1 == 0:
                print('(', a, b, int(c),')', end=' ')

n = input("What is the upper limit? ")
pythagoras(n)