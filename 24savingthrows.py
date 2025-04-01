# Title: 24 Saving Throws
# Author: Dean A

import random
import math
  


dc = int(input("What's the DC? "))
adv = input("Do you have advantage on this roll? (Y or N)")

for i in range(1):
    roll = random.randint(1, 20)
    if roll >= dc:
        print("You beat the DC of", dc, "with a roll of", roll)
    else:
        print("you only rolled a",roll, "YOU FAILED A DC", dc, "check ...idiot")






