# Title: 22 Fibonacci
# Author: Dean A

import math
import random

def fib_sequence(n): # n = number of digits you want listed
    a, b = 0 , 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    return ' '
    
print(fib_sequence(10))