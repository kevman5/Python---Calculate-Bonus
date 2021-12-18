# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 16:32:10 2021

@author: kevmm
"""

import math

def calcbonus():
    sales = 999
    while sales != -1 and sales < 9999:       
        
        sales = float(input("Enter sales( enter -1 to quit): "))
        
        if sales > 9999:
            totalbonus = sales * 0.01
            print("Your bonus is :", totalbonus)
        else:
            print("Your bonus is 0")
    
calcbonus()