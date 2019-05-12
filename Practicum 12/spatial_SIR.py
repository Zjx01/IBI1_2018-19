# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:21:46 2019

@author: Jessi
"""
import numpy as np 
import matplotlib . pyplot as plt
# make array of all susceptible population 
population = np. zeros ( (100 , 100) )
#the combination function in itertools can also be used here as replacement
outbreak = np.random. choice (range(100) ,2) #randomly select from the x and y coordinates of where the outbreak is happening
print(outbreak)
# the person with those exact coordinates in our population array and change their status from 0 (susceptible) to 1 (infected)
population [outbreak[0],outbreak[1]] = 1
β=0.3
γ=0.05
infectionN=[np.array[outbreak[0],outbreak[1]]]#to store the location of initial infection place
susceptible=[nparray中其他的点]
recover=[]
for i in range(100):#the time course is 100 days 
    for j in infectionN：#被感染个体周围的个体可用set储存，set可以排除重复的值
    infection=np.random.choice([infected,uninfected],被感染个体周围的八个个体,p=[β,1-β])
       for element in infection:
           if element=infected:
               infectionN.append()
               susceptible.pop()
           if element=uninfected:
               infectionN=infectionN
               susceptible=susceptible
    #所有患病者的位置都储存在一个列表中，最后在population函数中转化
    recovery=np.random.choice([infected,recover],len(感染者),p=[1-γ，γ])
       for patient in recovery:
           if patient=infected:
               感染者=感染者
           if patient=recovery:
               感染者.pop()
               recover.append()
               #append的对象应为recover的人的位置
               
plt . figure ( figsize =(6 ,4) , dpi=150) 
plt . imshow( population , cmap='viridis',interpolation='nearest' )
    
      
    
    
    
    
    
    
    
    
    
    









