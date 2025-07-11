# Title: 23 Triples
# Author: Dean A

# no inputs (can cause problems later), want everything on the command line
# functions used over again, otherwise don't

import math

def pythagtrips(n):
    x = int(n)
    for a in range(1,x):
        for b in range(a,x):
            c = math.sqrt(a**2 + b**2)
            if c % 1 == 0:
                print('(', a, b, int(c),')', end=' ')

pythagtrips(10)
