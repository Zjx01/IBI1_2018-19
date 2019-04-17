# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 17:08:11 2019

@author: Jessi
"""
n=2019
n0=n
sign=0 #用于储存n是奇是偶
answer=str(n) + "="

if n%2 != 0:
    n = n-1 #转换成偶数有助于while循环
    sign = 1 

while n != 0:
    j=0
    while j <= 13:
        if n0/2 >= 1:
            n0 = n0/2
            j = j+1
        else:
            break
    answer = answer + "+2^" + str(j)
    n = n - 2**j
    n0 = n

if sign == 1:
    answer = answer + "2**0"    
    
print(answer) 
        
            
        
    
