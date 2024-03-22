#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    
    total_weight = 0
    weighted_sum = 0
    
    for pair in my_list:
        weighted_sum += pair[0] * pair[1]
        total_weight += pair[1]
    
    if total_weight == 0:
        return 0
    
    return weighted_sum / total_weight
