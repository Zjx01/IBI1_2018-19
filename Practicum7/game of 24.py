# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 23:06:54 2019

@author: Jessi
"""
#to choose 2 numbers from the array and choose (+-*/)
#do the binary calculation of the two numbers
#Change list: remove the two Numbers in this array and put the calculatuon result into the list
#the new list will also undergo the former procedure 
n=input("please input the number to compute 24(use ',' to divide them):" )
a=n.split(',')
b=[int(i) for i in a]
#b=list(map(int,a))
#we need to judge whether the number we print in is qualified, ranged in(1,24)
for i in b:
    if i in range(1,24):
        i==i
    else:
        b.remove(i)
print("the list of number(from 1 to 23) put in",b) 
import itertools
c=b[:] 
recursion=0
def function(c):#change the function
    l=itertools.combinations(c,2)
    #to obtain all the combinations types of the chosen number
    c=b[:] 
    s=list(l)
    for elem in s:#the number in one combinition
        d=[elem[0]+elem[1],elem[0]-elem[1],elem[0]*elem[1],elem[0]/elem[1],elem[1]-elem[0],elem[1]/elem[0]]
        print ('the deposition with the chosen two number',d)
        c.remove(elem[0])
        c.remove(elem[1])
        s.remove(elem)
    #we need to pay attention to the a=0
        for i in range(len(d)):
            c.append(d[i])
        if len(c)==1:
           print(c[0]==24)
           recursion+=1
    function(c)
function(c)    

print('recursion=',recursion)

            #当只剩下一个数字的时候，再使用一个大循环，来判断最后的那个值是否=24

    
    
    
             
        
       
            
            
            
    

              
                  
    
       
         
    
    
    


    
    
    
     
    




        
    
    

