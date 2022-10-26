# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 14:14:56 2022

@author: TOBBY
"""

scores = [5,5,5,5,5,3,5,5,3]

total = 0
for score in scores:
    total += score
print(f"total: {total/9}")