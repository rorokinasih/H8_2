# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 11:10:36 2022

@author: User
"""

# Function definition is here
def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    total2 = total + arg1
    print("Inside the function : ", total)
    return total2

# Now you can call sum function
jumlah_keseluruhan = sum(10, 20)
print("Outside the function : ", jumlah_keseluruhan)