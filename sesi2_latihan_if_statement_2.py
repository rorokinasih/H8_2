# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 15:34:58 2022

@author: User
"""

nilaiabsen = int(input("nilai absen = "))
nilaitugas = int(input("nilai tugas = "))
nilaiuts = int(input("nilai uts = "))
nilaiuas = int(input("nilai uas = "))
nilaitotal = (nilaiabsen*0.1 + nilaitugas*0.2 + nilaiuts*0.3 + nilaiuas*0.4)

print("total nilai = ", nilaitotal)

if nilaitotal >= 80 <= 100:
    print("Anda Mendapatkan Grade A")
elif nilaitotal >= 70 <= 79:
    print("Anda Mendapatkan Grade B")
elif nilaitotal >= 60 <= 69:
    print("Anda Mendapatkan Grade C")
elif nilaitotal >= 50 <=59:
    print("Anda Mendapatkan Grade D")
else :
    print("Anda Mendapatkan Grade E")
