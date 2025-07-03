### 11Oligo.py by Dean Abdelnaby ###

#What is the melting temp of an oligo


# Equations based on total length number
def Tm(A, G, C, T):
    if (A + G + C + T) <= 13: return ((A + T)*2 + (G + C)*4)
    else: return round((64.9 + 41*(G + C - 16.4) / (A + T + G + C)), 4)
                    
# Input prompts for ACGT Numbers       
a = input('How many As are in the Oligo? ')
c = input('How many Cs are in the Oligo? ')
g = input('How many Gs are in the Oligo? ')
t = input('How many Ts are in the Oligo? ')

# Make sure all inputs are type(int)
A = int(a) 
C = int(c)
G = int(g)
T = int(t)

print(Tm(A, G, C, T))

print(Tm(1,2,3,4))