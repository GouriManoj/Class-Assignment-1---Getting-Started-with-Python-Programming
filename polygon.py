# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:41:31 2020

@author: Gouri Manoj
"""

class Polygon:
    def _init_(self,number,name):
        self.number = number
        self.name=name
        self.sides=[]
    def inputSides(self):
        print(self.name)
        for i in range(0,self.number):
            a=float(input("Enter side "+str(i+1)+" : "))
            self.sides.append(a)
class Triangle(Polygon):
    def _init_(self):
        Polygon._init_(self,3,"TRIANGLE :")

    def triArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)(s-b)(s-c)) ** 0.5
        print("The area of the triangle",self.area)

class Square(Polygon):

    def _init_(self):
        Polygon._init_(self,2,"SQUARE:")
    
    def sqArea(self):
        a, b = self.sides
        area=a**2
        print("The area of square is",self.area)


ob = Triangle()
ob.inputSides()
ob.triArea()
ob1 = Square()
ob1.inputSides()
ob1.sqArea()