# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:34:47 2019

@author: Emily
"""
import math
constant = (math.sqrt(2) * 2)/9801
inverse_of_pi = 0
for k in range(3):
    numerator1 = math.factorial(4 * k)
    numerator2 = 1103 + (26390 * k)
    numerator = numerator1 * numerator2
    denominator1 = (math.factorial(k)) ** 4
    denominator2 = 396 ** (4 * k)
    denominator = denominator1 * denominator2
    total = numerator/denominator
    inverse_of_pi += total
    #print(total)
a = constant * inverse_of_pi
print(1/a)    
difference = math.pi - (1/a)
print(difference)