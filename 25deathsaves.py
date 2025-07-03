# Title: 25 Death Saving Throws
# Author: Dean A

import random
import math
  


#dc = int(input("What's the DC? "))
#adv = input("Do you have advantage on this roll? (Y or N)")

def deathsavingthrow():
    fail = 0
    save = 0
    while fail < 3 and save < 3:
        roll = random.randint(1, 20)
        print(roll)
        
        if roll <= 9: fail = fail + 1
        elif roll == 20: return print("You are ALIVE and breathing")
        else: save = save + 1
    if save > fail: return print("You are STABLE but unconcious")
    else: return print("You are DEAD!")

deathsavingthrow()