# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:21:46 2019

@author: Jessi
"""
import numpy as np 
import matplotlib . pyplot as plt
# make array of all susceptible population 
population = np. zeros ( (100 , 100) ) 
# the person with those exact coordinates in our population array and change their status from 0 (susceptible) to 1 (infected)
#the combination function in itertools can also be used here as replacement
outbreak = np.random. choice (range(100) ,2) #randomly select from the x and y coordinates of where the outbreak is happening
population [outbreak[0],outbreak[1]] = 1
#print(outbreak)
β=0.3
γ=0.05
for i in range(100):#the time course is 100 days   
    infectionN = np.where(population==1)#to store the location of initial infection
#print(infectionN)
    susceptible=np.where(population==0)
#print(susceptible)
    recover=[]
    for j in range(len(infectionN[0])):#the susceptible individual location around infected individual can be store in set to evacuate the repetition 
       x=infectionN[0][j]
       y=infectionN[1][j]
       ## infect 8 neighbours each with probability beta
       for xNeighbour in range(x-1,x+2):
           for yNeighbour in range(y-1,y+2):
                if (xNeighbour,yNeighbour) != (x,y):#do not infect yourself but it does not really matter, because your value is already 1
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:#the edge point do not have 8 neighbors
                        if population[xNeighbour,yNeighbour]==0:#only susceptible neighbor can be infected
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-β,β])[0] 
       if population[x,y]==1:#the infected people stay ill or recover
          population[x,y]=np.random.choice([1,2],1,p=[1-γ,γ])[0]#np.random.choice put out a list     
#Label=['susceptible','infected','recover']
plt . figure ( figsize =(6 ,4) , dpi=150) 
plt . imshow( population , cmap='viridis',interpolation='nearest' )   
        
          
          
       
    
    
                                
"""       
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
      
"""
    
    
 



 

 
    
    
    
    
    









