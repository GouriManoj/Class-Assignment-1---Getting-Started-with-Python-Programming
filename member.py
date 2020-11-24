# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:26:20 2020

@author: Gouri Manoj
"""

class Member:
    def _init_(self, name, age, phonenumber, address, salary):
        self.name = name
        self.age = age
        self.phonenumber=phonenumber
        self.address=address
        self.salary=salary
    
    def printSalary(self):
        print("Salary : ",self.salary)



class Employee(Member):  # Inheritance
    def _init_(self, specialization):
        super()._init_("Gouri", 30, 9253748274,"XYZ",33000)
        self.specialization = specialization

    def report(self):
        print("Spetialization : ",self.specialization)
        print("Name:", self.name)
        print("age:", self.age)
        print("phone number:", self.phonenumber)
        print("Address:", self.address)
        print("Salary:", self.salary)


class Manager(Member):  # Inheritance
    def _init_(self, department):
        super()._init_("Gouri", 40,9253748274,"WTH",46000)
        self.department = department

    def report(self):
        print("Department : ", self.department)
        print("Name:", self.name)
        print("age:", self.age)
        print("phone number:", self.phonenumber)
        print("Address:", self.address)
        print("Salary : ",self.salary)


a = Employee("Programmer")
print(a.report())
b = Manager("Human Resources")
print(b.report())