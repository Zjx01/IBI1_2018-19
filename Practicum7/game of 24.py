# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 23:06:54 2019

@author: Jessi
"""
#从数组中取出两个数字，先对他们进行二元运算
#(2.1.1) 根据此排列的两个数字和运算符，计算结果
#(2.1.2) 改表数组：将此排列的两个数字从数组中去除掉，将 2.1.1 计算的结果放入数组中
#(2.1.3) 对新的数组，重复步骤 2
#(2.1.4) 恢复数组：将此排列的两个数字加入数组中，将 2.1.1 计算的结果从数组中去除掉
n=input("please input the number to compute 24:(use ',' to divide them)" )
a=n.split(',')
b=[int(i) for i in a]
#b=list(map(int,a))
print(b)
#we need to judge whether the number we print in is qualified, ranged in(1,24)
print("the input number must be integer from 1 to 23" )

for i in b:
    if i in range(1,24):
        i=i
    else:
        b.remove(i)
        print(b)
c=b[:]   
import itertools
#operator=['+','-','*','/']

#for j in range(int(len(b))):
l=itertools.combinations(b,2)
print ('l=',l)
s=list(l)
print('s=',s)
#name 'c' undifined, move the definitionof c out of the circulation,so it is defined
for elem in s:
    w=0
    c=b[:]
    #是e也进入这个循环
    d=[elem[0]+elem[1],elem[0]-elem[1],elem[0]*elem[1],elem[0]/elem[1],elem[1]-elem[0],elem[1]/elem[0]]
    print ('对取出取出两数的加减乘除的操作',d)
    print ('elem=', elem)
    c.remove(elem[0])
    c.remove(elem[1])
    print("移除元素后的列表",c)
    #we need to pay attention to the a=0
     #unsupported operand type(s) for-: 'str' and 'str', the species of a(str) need to be converted
#problems:不知道为什么这里不能一个一个地将d中地值循环，和下面脱节了
    for i in range(len(d)):
        e=c[:]
        e.append(d[i])
        print('加入新的元素',e)
        if len(e)==1:
           print(e[0]==24)
           print("recursion times:",w)
           w=w+1
        else:
           continue
            #当只剩下一个数字的时候，再使用一个大循环，来判断最后的那个值是否=24
    
    
             
        
            
            
            
            
            
    

              
                  
    
       
         
    
    
    


    
    
    
     
    




        
    
    

