##10demo.py by Dean Abdelnaby
def isinteger(a):
    if a % 1 == 0 and a // 1 == a:
        return True
    else:
        return False
# a = input('Is x an integer? x = ') 

def isprobability(b):
    if 0 <= b <= 1:
        return True
    else:
        return False
# b = input('Is my number a probability?')

def dnaweight(d):
    if d == 'A' or d== 'a' or d== 'Adenine' or d== 'adenine':
        return print('Adenine in DNA has a molecular weight of 135.13 g/mol')
    elif d == 'C' or d== 'c' or d== 'Cytosine' or d== 'cytosine':
        return print('Cytosine in DNA has a molecular weight of 111.10 g/mol')
    elif d == 'G' or d== 'g' or d== 'Guanine' or d== 'guanine':
        return print('Guanine in DNA has a molecular weight of 126.11 g/mol')
    elif d == 'T' or d== 't' or d== 'Thymine' or d== 'thymine':
        return print('Thymine in DNA has a molecular weight of 151.13 g/mol')
    else: return print(None)

#d = input('What is the molecular weight of ')
# dnaweight(d)
def dnantmatch(e):
    if e == 'A' or e== 'a' or e== 'Adenine' or e== 'adenine':
        return print('Thymine')
    elif e == 'C' or e== 'c' or e== 'Cytosine' or e== 'cytosine':
        return print('Guanine')
    elif e == 'G' or e== 'g' or e== 'Guanine' or e== 'guanine':
        return print('Cytosine')
    elif e == 'T' or e== 't' or e== 'Thymine' or e== 'thymine':
        return print('Adenine')
    else: return print(None)
# e = input('What is the DNA base pair for ')
# dnantmatch(e)

def thelargest(a, b, c):
        if a == b == c: print('They are all the same')
        elif b < a and a > c: print(a)
        elif a < b and b > c: print(b)
        elif b < c and a > a: print(c)
        elif b == a and a > c: print(a)
        elif a < b and b == c: print(b)
        elif b < c and c == a: print(c)
   

# a = input('What is the 1st number? ')
# b = input('What is the 2nd number? ')
# c = input('What is the 3rd number? ')
# thelargest(a, b, c)


##-----------------------------------------------------------------------##

