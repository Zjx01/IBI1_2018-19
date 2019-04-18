# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:02:27 2019

@author: Jessi
"""
#Tips: pyplot.pie 
#Given: A DNA string s of length at most 1000 nt. 
s=input()
myDict={}
for word in s:
        if word in myDict:
            myDict[word] +=1
            #operator +=:   x+=5 -> x=x+5
        else:
            myDict[word]=1
print(myDict)
import matplotlib.pyplot as plt
#frequency= tuple(myDict.values) the percentage will be calculated later in the autopct='%1.1f%%'
#
labels=['A','C','G','T']
size=myDict.values()
explode=(0,0.1,0,0)
plt.pie(size,explode=explode,labels=labels,autopct='%1.1f%%')
plt.show()
#when run the program,the content need to be typed in by yourself, after which you should press the button enter 








    
            
            

