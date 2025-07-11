# Title: Practice Problems for Unit 2
# Author: Dean Abdelnaby

# 1) Write a function that calculates the triangular number. This is the sum of n.

# 1 -> n, add 1+2+...+n
import math
def triadd(n): return n * (n + 1) // 2
        
def triadd_loop(c):
    x = 0
    for i in range(c + 1):
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
# 4) Write a function that solves "n choose k": n! / k!(n - k)!
def nchoosek(n,k):
    x = factorial(k) * factorial(n - k)
    return (factorial(n) / x)

# 5) Write a function that estimates Euler's number: e (2.71828...). This can be computed as the infinite sum of 1/n!. Choose a finite number of iterations.
def eulers(n):
    x = 0
    for i in range(n):
        x += 1 / factorial(i)
    return x

# 6) Write a function to determine if a number is prime.

def isprime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0: return False
    return True

# 7) Write a function that estimates Pi (3.14159...) using the Nilakantha series. Again, choose a finite limit. Pi = 3 + 4/(2x3x4) - 4/(4x5x6) + 4/(6x7x8) - 4/(8x9x10) ...

def pi_approx(x):
    pi = 3
    for i in range(1, x+1):
        n = 2 * i
        d = n * (n+1) * (n+2)
        if i % 2 == 0: pi = pi - 4 / d
        else:          pi = pi + 4 / d
    return pi