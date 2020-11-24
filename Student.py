# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:58:06 2020

@author: Gouri Manoj
"""

class Student:
    def fillDetails(self):
        self.name = input("Enter your name : ")
        self.age = input("Enter your age : ")
        self.address = input("Enter your address : ")
    def displayDetails(self):
        print(f"Name : {self.name}\nAge : {self.age}\nAddress : {self.address}\n")

class Sports():
    def accept_sportsmark(self):
        self.mark = int(input("Enter the Sports mark : "))
    
    def display_sportsmark(self):
        print("Sports mark is {self.mark}")


class Statement(Student, Sports):
    def accept_mark(self):
        self.m1 = int(input("Enter the Mark of Subject 1 : "))
        self.m2 = int(input("Enter the Mark of Subject 2 : "))
        self.m3 = int(input("Enter the Mark of Subject 3 : "))

    
    def display_total(self):
        self.Total = self.m1+self.m2+self.m3+self.mark
        print("{self.name}\'s Total marks is {self.Total}")