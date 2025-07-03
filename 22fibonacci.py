# Title: 22 Fibonacci
# Author: Dean A

import math
import random

def fib_sequence(n): # n = number of digits you want listed
    list1 = [0, 1]
    a, b = 0 , 1
    for i in range(n):
        a, b = b, a + b
        list1.append(b)
    return print(list1)
    
print(fib_sequence(29))