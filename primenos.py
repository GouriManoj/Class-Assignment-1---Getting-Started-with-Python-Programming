# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 11:58:48 2021

@author: Gouri Manoj
"""

r=int(input("Enter upper limit: "))
for a in range(2,r+1):
    k=0
    for i in range(2,a//2+1):
        if(a%i==0):
            k=k+1
    if(k<=0):
        print(a)
