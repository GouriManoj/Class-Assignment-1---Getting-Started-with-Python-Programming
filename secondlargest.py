# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 09:03:10 2020

@author: Gouri Manoj
"""

list1 = [11,22,1,2,5,67,21,32]
# to get unique elements
new_list = set(list1)
# removing the largest element from list1
new_list.remove(max(new_list))
# now computing the max element by built-in method?
print(max(new_list))