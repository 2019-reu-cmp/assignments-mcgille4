# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:15:32 2019

@author: Emily
"""
#Read the contents of the file.
with open('sunspots.txt', 'r') as f:
    entire_file = f.read()
list_of_data = entire_file.split("\n")
#Dictionary not necessary for this application, but useful for other applications.
dict_of_sunspots = {}
#List containing the daily sunspot values.
sunspot_values_list = []
#Add data which was read from file to list.
for n in list_of_data:
    n = n.split("\t")
    dict_of_sunspots[int(n[0])] = float(n[1])
    sunspot_values_list.append(float(n[1]))
print(sunspot_values_list)
#Average = mean = total number of sunspots/total number of days.   
#Add up total number of days.
number_of_days = len(sunspot_values_list)
#Add up total number of sunspots.
spot_sum = 0
for item in sunspot_values_list:
    spot_sum += item
#Calculate and return mean.    
average_spot = spot_sum / number_of_days    
print("Average of number of sunspots: " + str(round(average_spot, 2)))
#Implement a count(high, low) function which returns the number of days with sunspots above low and above high.
def count(low, high, data = sunspot_values_list):
    too_low = 0
    too_high = 0
    for n in data:
        if n < low:
            too_low += 1
        elif n > high:
            too_high += 1
    within_range = len(data) - (too_low + too_high)
    return within_range

print(count(40, 60))      
            
        