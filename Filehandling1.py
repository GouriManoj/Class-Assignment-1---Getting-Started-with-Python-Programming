# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 07:52:52 2020

@author: Gouri Manoj
"""
file1 = open("C:\\Users\\GouriManoj\\Documents\\file1.txt","w")
file1.write("%d %d %d %d %d" %(8,1,3,2,1))
file1.close()
file1 = open("C:\\Users\\GouriManoj\\Documents\\file1.txt","r")
s = file1.readline()
s = s.split(" ")
t =[int(i) for i in s]
t.sort()
j =[]
for b in t:
   if b not in j:
       j.append(b)
file1.close()
file1 = open("C:\\Users\\GouriManoj\\Documents\\file1.txt","w")
file1.write(j)
file1.close()
file1 = open("C:\\Users\\GouriManoj\\Documents\\file1.txt","r")
h = ','.join(str(o) for o in j)
file1.close()
file1 = open("C:\\Users\\GouriManoj\\Documents\\file1.txt","w")
file1.write(h)
7
file1.close()
def copyFile(oldFile, newFile):
  f1 = open(oldFile, "r")
  f2 = open(newFile, "w")
  while True:
    text = f1.read(50) #text = f1.readline()
    if text == "":
      break
    f2.write(text)
    f1.close()
    f2.close()
    return
copyFile("C:\\Users\\GouriManoj\\Documents\\file1.txt","C:\\Users\\GouriManoj\\Documents\\file2.txt")
file2 = open("C:\\Users\\GouriManoj\\Documents\\file2.txt","r")
print(file2.read())
1,2,3,8
