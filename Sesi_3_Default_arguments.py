# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:15:21 2022

@author: User
"""

# Function definition is here
def printinfo( name, gender, age = 26):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age: ", age)
   print("gender: ", gender)
   return;

# Now you can call printinfo function
printinfo( age=50, name="hacktiv8" , gender="female")
printinfo( name="hacktiv", gender="male" )
printinfo( name="hacktiv4", gender="male" )