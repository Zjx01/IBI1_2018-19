# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 17:08:11 2019

@author: Jessi
"""
n=eval(input("input a integer:",))
n0=n
sign=0 #to store whether the number input is an odd or even
answer=str(n) + "="

if n%2 != 0:
    n = n-1
#to change the odd number into even, and the minused 1 will be added by sign a the end of the function
    sign = 1 
while n != 0:#the garantee of the function 
    j=0
    while j <= 13:
        if n0/2 >= 1:#to find the biggest 2**n in the n given, by dividing 2 continuoyly and compare with 1
            n0 = n0/2
            j = j+1
        else:
            break
    answer = answer + "+2**" + str(j)
    n = n - 2**j #the remaining value after getting rid of the biggest 2**n
    n0 = n

if sign == 1:
    answer = answer + "+2**0"    
print(answer) 
        
            
        
    
