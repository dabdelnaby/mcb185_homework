# Title: 30demo
# Author: Dean A
import math

# Write a funct that reutrns the minimum value of a list

list1 = [1,2,3,4]

def minimum(n):
    mini = n[0]
    for val in n[1:]:
        if val < mini: val = mini
    return mini

# Write a function that returns both the min and mex values of a list

def minmax(n):
    mini = n[0]
    maxx = n[0]
    for val in n[1:]:
        if val < mini: mini = val
        elif val > maxx: maxx = val
    return mini, maxx

# Write a funct that returns the mean of the values in a list

def listmean(list):
    n = 0
    for val in list:
        n += val
    meanval = n / len(list)
    print(meanval)

# Write a function that computes the entropy of a probabulity distribution


def entropy(probs):
    h = 0
    for p in probs:
        h -= p * math.log2(p)
    return h
print(entropy([0.8, 0.1, 0.1]))

# Write a funct that computes the KL distance between 2 sets of prob distributions

def dkl(prob1, prob2):