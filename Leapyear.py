# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 08:36:27 2021

@author: Gouri Manoj
"""
year=int(input("Enter year"))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
