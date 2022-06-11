# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:43:49 2022

@author: User
"""

# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print("Output is: ")
   print(arg1)
   for var in vartuple:
      print(var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, "a" )

# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print("Output is: ")
   print(arg1)
   for var in vartuple:
      print(var)
   return;

# Now you can call printinfo function
printinfo( 10 , 20)
# printinfo( 70, 60, 50, "a" )

# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print("Output is: ")
   print(arg1)
   for abc in vartuple:
      print(abc)
   return;

# Now you can call printinfo function
printinfo( 10 , 20,"a")
# printinfo( 70, 60, 50, "a" )