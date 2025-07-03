# Title: 24 Saving Throws
# Author: Dean A

import random


def savingthrow():
        dc = int(input("What's the DC? "))
        adv = input("Do you have advantage on this roll? (Y or N)")
        roll = random.randint(1, 20)
        roll2 = random.randint(1,20)

        if adv == "Y": 
                if roll >= dc or roll2 >= dc:
                        return print("You beat the DC of", dc, "with a roll of", roll, "or", roll2)
                else:
                        return print("you only rolled a",roll, "or", roll2, "YOU FAILED A DC", dc, "check")
        else:
                if roll >= dc:
                        return print("You beat the DC of", dc, "with a roll of", roll)
                else:
                        return print("you only rolled a",roll, "YOU FAILED A DC", dc, "check")

savingthrow()