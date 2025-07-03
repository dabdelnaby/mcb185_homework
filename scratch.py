# Title: Practice/Scratch Paper for MCB185
# Author: Dean A
## isprime() = write a function that returns 'True' if a number is prime and false if not ##
'''
def is_prime(x):
   
    if x == 2 or x == 3 or x == 5 or x == 7: return print('True')
    elif x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0: return print('False')
    else: return print('True')

def is_prime2(x):
    if x == 1: return print('False')
    for den in range(2,x):
        if x % den == 0: return print('False')
    else: return print('True')



#is_prime(y)

#Factorial

def fac(x):
    for n in range(1,x):
        x *= n
    return print(x)

#y =input('What is the factorial of: ')
#z = int(y)

import math
import random

def pythagoras(n):
    x = int(n)
    for a in range(1,x):
        for b in range(a,x):
            c = math.sqrt(a**2 + b**2)
            if c % 1 == 0:
                print('(', a, b, int(c),')', end=' ')

x = random.random()
y = random.random()
'''


import argparse

parser = argparse.ArgumentParser(description='Finds games that are possible')
parser.add_argument('file', help='Input the file')
arg = parser.parse_args()


A = 0
C = 0
G = 0
T = 0
def ntcounter():
    with open(arg.file) as fp:
        for line in fp:
            for _ in line:
                if _ == 'A':
                    A += 1
                if _ == 'C':
                    C += 1
                if _ == 'G':
                    G += 1
                if _ == 'T':
                    T += 1
        print(A,C,G,T)

def antistrand():
    seq = ''
    with open(arg.file) as fp:
        for line in fp:
            for _ in line:
                if _ == 'T':
                    seq += _.replace('T','A')
                if _ == 'A':
                    seq += _.replace('A','T')
                if _ == 'C':
                    seq += _.replace('C','G')
                if _ == 'G':
                    seq += _.replace('G','C')
            print(seq[::-1])
