# Assessment 2 
# Author - Dean Abdelnaby


def maxim(a,b,c,d):
    if a >= b and a >= c and a >= d: return a
    if b >= c and b >= d: return b
    if c >= d: return c
    return d
#print(maxim(1,3,5,12))


# write the numebrs 1-50, if number is prime follow with '!'

#for n in range(1,11):
    #if n == 1 or n == 2 or n == 3 or n == 5 or n == 7: print(n)
    #if n % numb == 0: print(n)
    #else: print(str(n)+'!')

def is_prime(x):
    for i in range (2, x//2 +1):
        if n % i == 0: return False
        return True
    print(True)
  
is_prime(10)

     