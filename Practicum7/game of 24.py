# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 23:06:54 2019

@author: Jessi
"""
#to choose 2 numbers from the array and choose (+-*/)
#do the binary calculation of the two numbers
#改表数组：将此排列的两个数字从数组中去除掉，将 2.1.1 计算的结果放入数组中
#(2.1.3) 对新的数组，重复步骤 2
#(2.1.4) 恢复数组：将此排列的两个数字加入数组中，将 2.1.1 计算的结果从数组中去除掉
n=input("please input the number to compute 24(use ',' to divide them):" )
a=n.split(',')
b=[int(i) for i in a]
#b=list(map(int,a))
#we need to judge whether the number we print in is qualified, ranged in(1,24)
print("the input number must be integer from 1 to 23" )
for i in b:
    if i in range(1,24):
        i=i
    else:
        b.remove(i)
    print("the list of number put in",b) 
import itertools
c=b[:] 
def function(c):#change the function
    l=itertools.combinations(b,2)
    recursion=0
    c=b[:]  
    #to obtain all the combinations types of the chosen number
    s=list(l)
    for elem in s:#the number in one combinition
        d=[elem[0]+elem[1],elem[0]-elem[1],elem[0]*elem[1],elem[0]/elem[1],elem[1]-elem[0],elem[1]/elem[0]]
        print ('the deposition with the chosen two number',d)
        e=c.remove(elem[0])
        e=e.remove(elem[1])
        print("the list after removal of used elements",e)
    #we need to pay attention to the a=0
    for i in range(len(d)):
        e.append(d[i])
        if len(e)==1:
           print(e[0]==24)
           recursion+=1
function(c)
    
            #当只剩下一个数字的时候，再使用一个大循环，来判断最后的那个值是否=24

    
    
    
             
        
            
            
            
            
            
    

              
                  
    
       
         
    
    
    


    
    
    
     
    




        
    
    

