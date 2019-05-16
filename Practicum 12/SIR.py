# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:08:27 2019

@author: Jessi
"""

import numpy as np 
import matplotlib . pyplot as plt

#susceptibleN=['1'*999]
"""
1 represent people  suscepticle to disease
0 represent people  infected
2 represent people recovered
"""
β=0.3
γ=0.05
N=10000#sum of the population involved
I=[0]#list store people get ill
S=[1] * 9999#people who is healthy
R=[]#people recovered
A=[9999]
B=[1]
C=[0]
"""
these initial numbers should be out of the loop or it will goes into the loop every time
"""
#A,B,C are used to store the length of list of infectious and recovered people
for i in range(0,1000):
    a=np.random.choice(range(2),len(S),p=[β*len(I)/N,1-β*len(I)/N])
    #susceptible individuals have chances to get disease and recover
    for j in a:
        if j==0:
            I.append(0)#append the people newly infected and delete them from the susceptible populations
            S.pop()
        if j==1:
            S=S
    b=np.random.choice([2,0],len(I),p=[γ,1-γ])
    #infected individuals have chances to recover or stay ill
    for e in b:
        if e==2:
            R.append(2)#to append the newly recovered people and delete it in the infectious number
            I.pop()   
        if e==0:
            I=I
    A.append(len(S))
    B.append(len(I))
    C.append(len(R))
print('the number of susceptible',A)
print('the number of infectious',B)
print('the number of recover',C)

#plot
plt.figure(figsize=(6,4),dpi=150)
X=list(range(0,1001))
susceptibleN,infectiousN,recoverN=A,B,C
plt.xlabel("times", fontsize=14)
plt.ylabel("number of people", fontsize=14)
plt.title("SIR model")
plt.plot(X,susceptibleN)
plt.plot(X,infectiousN)
plt.plot(X,recoverN)
plt.legend(["susceptible","infected","recover"],loc='upper right')  
plt.savefig ("markflow1" ,type="png")
plt.show()

















"""
abandoned code
---------------
import collections
there is no need to use function to solve this problem
#infectiousN=['0'*1]
#RecoverN=[0]
#N=[susceptibleN,infectiousN,RecoverN]
susceptible=999
infectious=1
recover=0
susceptible=999
infectious=1
β=0.3
i=0
def infectious(susceptible,infectious):
    while i in range(0,1000):
          newInfectious=0
          I=[]
          S=[]
          a=np.random.choice(range(2),1000,p=[β,1-β])
          newInfectious=newInfectious+collections.Counter(1 in a)
          infectious=infectious+newInfectious
          susceptible=susceptible-collections.Counter(0 in a)
          i+i+1
    I=I.append(infectious)
    S=S.append(susceptible)
    def Recoverage(infectious,recover):
        R=[]
        recover=0
        gamma=0.05
        while i in range(0,1000):  
              b=np.random.choice(range(1,3),len(susceptible),p=[gamma,1-gamma])
              recover=recover+collections.Counter(2 in b)
              susceptible=susceptible-recover
              i+i+1
        R=R.append(recover)
        S=S.append(susceptible)
infectious(susceptible,infectious)
Recoverage(infectious,recover)
"""

    

        
          
          
    
    
         

    
    
    
    
    
    
    
    
   


    
    
    




