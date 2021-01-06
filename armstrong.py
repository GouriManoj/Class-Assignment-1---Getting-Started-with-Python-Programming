# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 11:48:08 2021

@author: Gouri Manoj"""
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
