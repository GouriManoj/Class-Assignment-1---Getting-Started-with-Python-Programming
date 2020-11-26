# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:19:18 2020

@author: Gouri Manoj
"""

class Digits():
    num=int()
    sum_of_num=int()
    def _init_(self):
        self.num=0
        self.sum_of_num=0

    def num_input(self):
        num = input("Enter the number")
        self.digit_sum(num)

    def digit_sum(self,num):
        sum_of_num=int(num)
        while int(sum_of_num) > 10:
            ls_dig = [int(x) for x in str(sum_of_num)]
            sum_of_num=sum(ls_dig)
            self.num_output(sum_of_num)

    def num_output(self,sum_of_num):
        print("SUM OF DIGITS:",sum_of_num)

p=Digits()
p.num_input()