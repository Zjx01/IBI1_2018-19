# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:16:39 2019

@author: Jessi
"""

import os
import numpy as np
os.chdir('C:/Users/Jessi/OneDrive/桌面/IBI/IBI1_2018-19/Practical13') 
def xml_to_cps():
    import os
    import xml.dom.minidom
    
    # first, convert xml to cps   
    os.system("CopasiSE.exe -i predator-prey.xml -s predator-prey.cps")
    
    # now comes the painful part. Just copy and paste this ok
    
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
        
    
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
           
            
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w")
    cpsTree.writexml(cpsFile)
    cpsFile.close()
#xml_to_cps()
import csv
csv_file = open('modelResults.csv', 'r') 
csv_reader_lines = csv.reader(csv_file) 
datelist=[]
day=[]
for one_line in csv_reader_lines:
    day.append(one_line)
    print(day)
datelist.append(day)
results = np.array (datelist)
Results = results.astype (np. float)
print(Results)
import matplotlib . pyplot as plt
#names=np.array('time','A','B')
time=[]
A=[]
B=[]
for i in datelist:# i is the list contain time, population of predator and prey at a time
    for j in i:
        time.append(float(j[0]))
        A.append(float(j[1]))
        B.append(float(j[2]))
    plt.figure(figsize=(6,4),dpi=150)
X=time
plt.xlabel("time", fontsize=14)
plt.ylabel("population size",fontsize=14)
plt.plot(A,label='predator(b=0.02.d=0.4)')
plt.plot(B,label='prey(b=0.1,d=0.02)')
plt.legend(loc='upper right')
for i in datelist:# i is the list contain time, population of predator and prey at a time
    for j in i:
        time.append(float(j[0]))
        A.append(float(j[1]))
        B.append(float(j[2]))
    plt.figure(figsize=(6,4),dpi=150)
plt.xlabel("predator(b=0.02.d=0.4)")
plt.ylabel("prey(b=0.1,d=0.02)")
plt.title("time course")
plt.plot(A,B)
plt.title("cycle limit")

import xml.dom.minidom
DOMTree = xml.dom.minidom.parse("predator-prey-copy.xml")
# four parameter: k predator breeds, k predator dies, k prey breeds, k prey dies
major=DOMTree.documentElement
parameters=major.getElementsByTagName('Parameter')#nodelist of parameter
import random
for parameter in parameters:
    parameter.getAttribute('value')#get the attribute value
   #create a float range in (0,1) for value
    parameter.setAttribute('value',random.random())
    """
copy=open('predator-prey-copy.xml','w')#there is still some problem with write xml part which needs to be changed
DOMTree.writexml(copy)
copy.close()
xml_to_cps()
#to store the differences made to the copy
os.system("CopasiSE.exe predator-prey-copy.cps")#change it to the cps
import csv
csv_file = open('modelResults.csv', 'r') 
csv_reader_lines = csv.reader(csv_file) 
results = []
import numpy
for one_line in csv_reader_lines:
    results.append(one_line)
results_number=results[1:,1:3]
results_number=results_number.astype(numpy.float)
plt.plot(results_number[0:,0],label="prey")
plt.plot(results_number[0:,1],label="predator")
plt.xlabel('time')
plt.ylabel('population size')
plt.title('time course')
plt.legend()
 

what plan to do later  
--------------------------
change the xml file into the cps
plot the diagram 
on the basis of the first plot 
later can define a function, use global count to run 100 times, each time count=count+1,run the simulation
"""














