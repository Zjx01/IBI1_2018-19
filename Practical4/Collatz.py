# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:03:32 2019

@author: Jessi
"""

#n=5,use while-loop until we get 1,even should be divided by 2; if it is odd number, first multiplying 3 and adding 1 to be an even and divide 2 continuously
#while 1 is reached, it will constantly be 1-4-2-1-4-2, but we end the first time we reach 1 
n=input('please input a positive interger:')
n=int(n)
while n!=1:
    if n%2==0:
           n=n/2
    else:
           n=3*n+1
    print("n==",n)


  

