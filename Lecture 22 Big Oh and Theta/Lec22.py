# Lecture 22: Big Oh and Theta

import time
import math
def convert_to_km(m):
    return m * 1.609
def compound(invest, interest, n_months):
    total=0
    for i in range(n_months):
       total = total * interest + invest
    return total
L_N = [1]
for i in range(8):
    L_N.append(L_N[-1]*10)