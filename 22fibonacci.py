# Title: 22 Fibonacci
# Author: Dean A


def fib_sequence(n): # n = number of digits you want listed
    a = 0
    b = 1
    for i in range(n):
        f = b + a
        print(f)
        a = b
        b = f


fib_sequence(10)