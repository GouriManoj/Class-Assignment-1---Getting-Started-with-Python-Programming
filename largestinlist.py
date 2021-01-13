# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 08:46:25 2021

@author: Gouri Manoj
"""

list1 = [] 
  
num = int(input("Enter number of elements in list: ")) 
  
 
for i in range(1, num + 1): 
    ele = int(input("Enter elements: ")) 
    list1.append(ele) 
      

print("Largest element is:", max(list1)) 