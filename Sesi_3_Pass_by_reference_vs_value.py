# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 09:29:39 2022

@author: User
"""

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   #mylist.append([1,2,3,4]);
   mylist.append(1);
   mylist.append(2);
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
mylist = [70,80,90];
changeme( mylist );
print("Values outside the function: ", mylist)