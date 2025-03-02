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
    

print(pythagoras(3, 4))

## Practice

def circle_area(r): return math.pi * r**2
def rectangle_area(w,h): return w*h
def triangle_area(b,ht): return (b*ht)/ 2
def distance_between(x,y,t,u): return pythagoras((x-t),(y-u))

print("Find the area of a circle") # interactive circle area
r = input("enter radius:")
print("the area of the circle is", circle_area(float(r)))

print("Find the area of a rectangle")  # interactive rect area
w = input("enter width:")
h = input("enter height:")
print(rectangle_area(float(w),float(h)))

print("Find the area of a triangle")
b = input("enter triangle base length:") # interactive triangle area
ht = input("enter triangle height:")
print(triangle_area(float(b),float(ht)))

print("Find the distance between 2 points", "Enter the coordinates of the two points")
x = input("enter the X-value of the FIRST point:") # interactive distance between 2 points
y = input("enter the Y-value of the FIRST point:")
t = input("enter the X-value of the SECOND point:")
u = input("enter the Y-value of the SECOND point:")
print(distance_between(float(x), float(y), float(t),float(u)))