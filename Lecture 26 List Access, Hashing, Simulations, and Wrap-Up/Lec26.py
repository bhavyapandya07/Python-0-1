import random

def dice(side):
    dice = ['.', ':', ':.', '::', '::.', ':::']
    n = 7
    c = 0
    for i in range(n):
        roll = random.choice(dice)
        if roll == side:
            c += 1
    print(c / n)
dice('.')
dice('::')

#----

import random

def prob_dice_atleast(Nrolls, n_at_least):
    dice = ['.', ':', ':.', '::', '::.', ':::']
    Nsims = 1000000
    how_many_matched = []

    for _ in range(Nsims):
        matched = 0
        for _ in range(Nrolls):
            roll = random.choice(dice)
            if roll == '::':
                matched += 1
        how_many_matched.append(matched)
    
    at_least_this = sum(1 for count in how_many_matched if count >= n_at_least)
    print(at_least_this / Nsims)
prob_dice_atleast(10, 3)