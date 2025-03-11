# Title: Practice Problems for Unit 2
# Author: Dean Abdelnaby

# 1) Write a function that calculates the triangular number. This is the sum of n.

# 1 -> n, add 1+2+...+n
import math
def triadd(n): return n * (n + 1) // 2
        
def triadd_loop(c):
    x = 0
    for i in range(1, c + 1):
        x = x + i
    return x

# 2) Write a function that calculates the factorial of a number.

def factorial(n):
    x = 1
    for i in range(1, n+1):
        x = x * i
    return x

# 3) Write a function that computes the Poisson probability of k events occurring with an expectation of n: n^k e^-n / k!

def poisson(n, k):
    x = 1
    for i in range (1, k+1):
        x = x * 1
        z = (n ** k) * (math.e) ** ((-n) // x)
        return z
print(poisson(3, 6))