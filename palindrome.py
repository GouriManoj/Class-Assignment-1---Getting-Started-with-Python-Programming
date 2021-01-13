# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 08:44:05 2021

@author: Gouri Manoj
"""

def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s=str(input("Enter word"))
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")