# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 15:03:14 2021

@author: Henry
"""

import random

number = 0

for i in range(1, 100):
    number = random.randint(1,20)
    print("終極密碼為 : " + str(number))
    
count = 0
while True:
    guess = input("請輸入一個數字")
    guess = int(guess)
    if (guess) == number:
        print("你答對了!!!")
        break   
    else:
        print("你答錯了!!!")
    count = count + 1
    print(count) 
    if (count) == 5:
        break