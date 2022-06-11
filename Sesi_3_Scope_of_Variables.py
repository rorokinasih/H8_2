# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 11:18:42 2022

@author: User
"""

# total = 0; 

# def sum( arg1, arg2 ):

#    total = arg1 + arg2; 
#    print("Inside the function local total : ", total)
#    return total;

# # def min():
    

# sum( 10, 20 );
# print("Outside the function global total : ", total)

# jumlahKucing = 20

# def jumlahHewan():
#     jumlahAnjing = 30
#     return jumlahKucing + jumlahAnjing

# def jumlahKelinci():
#     return jumlahKucing + jumlahKucing

# print (jumlahHewan())
# print (jumlahKelinci())


jumlahKucing = 20

def jumlahHewan():
    jumlahAnjing = 30
    return jumlahKucing + jumlahAnjing

def jumlahKelinci():
    return jumlahKucing + jumlahKucing

print ((jumlahHewan(),jumlahKelinci(), jumlahHewan()+jumlahKelinci()))