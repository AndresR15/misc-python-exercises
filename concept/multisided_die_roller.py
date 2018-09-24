# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 17:11:28 2018

@author: andres15
"""

#multi-headed die roller

import sys
import numbers
import random
#need sys for command line arguments

def roll(n, x):
    #rolls x number of n-sided die 
    total = 0
    rolls = []
    for a in range(x):
        temp = random.randint(1, n)
        rolls.append(temp)
        total += temp
    return total, rolls

if len(sys.argv) > 3 or len(sys.argv) < 3:
    sys.exit("Error! Invalid number of arguments!")
elif not sys.argv[1].isdigit or not sys.argv[2].isdigit:
    sys.exit("Error! All arguments must be numbers")    

x, y = roll(int(sys.argv[1]), int(sys.argv[2]))
roll_list = ','.join(str(t) for t in y)
print(f'You rolled a total of {str(x)}, with the rolls: {roll_list}')




     