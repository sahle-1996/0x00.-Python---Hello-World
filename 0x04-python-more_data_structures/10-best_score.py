#!/usr/bin/python3

def best_score(my_dict):
    if my_dict:
        max_key = max(my_dict, key=my_dict.get)
        return max_key
    return None
