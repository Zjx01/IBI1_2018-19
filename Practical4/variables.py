# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:12:08 2019

@author: Jessi
"""

a=256
b=256256
if b%7==0:
    print("b can be divided by 7")
   
c=b/7
d=c/11
e=d/13 
print("c==",str(c), "d==",str(d), "e==",str(e))
print (e<a)

#after if, space back, the command can be carried out
    
#X and Y are random variables, variable Z encodes "(X and not Y) or (Y and not X)"
#W encodes "X!=Y"

X=True
Y=False
Z=(X and not Y) or (Y and not X)
print(Z)
W=(X!=Y)
print(W)







    
     