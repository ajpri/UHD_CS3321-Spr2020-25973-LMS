#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 11:51:57 2020

@author: austin
"""

grades = ("A", "C", "F")

def calcgpa(inputgrades):
        sum = 0
        for grade in grades:
            if grade.upper() == "A":
                sum += 4
            elif grade.upper() == "B":
                sum += 3
            elif grade.upper() == "C":
                sum += 2
            elif grade.upper() == "D":
                sum += 1
            elif grade.upper() == "F":
                sum += 0   
                
        return sum/len(inputgrades)
    
print(round(calcgpa(grades),2))
