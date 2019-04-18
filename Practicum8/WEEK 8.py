# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:06:38 2019

@author: Jessi
"""

from xml.dom.minidom import parse  
import xml.dom.minidom 
import pandas as pd
import re
DOMTree = xml.dom.minidom.parse("go_obo.xml")
root=DOMTree.documentElement
print(root)
terms=root.getElementsByTagName("term")
"""
to find out the element term with autophagosom first
"""

for term in terms:
    definition=term.getElementsByTagName('defstr')[0].childnodes[0]
    if re.findall(r'autophagosome',definition):
        id=term.getElementByTagName('id')[0].childnodes[0]
        name=term.getElementByTagName('type')[0].childnode[0]
    print(definition)
    print(id)
    print(name)
def childnode(is_a):
    for term in terms:
        
        
    
    
    
    
    
    
    

        



"""
content="<defstr>(.*?)</defstr>"
for a in term:
    id=[]
    name=[]
    definition=[]
    if re.match(r'<id>(.*?)</id>',str(a)):
        id.append()
        #incorrect <>
    if re.match(r'<name>(.*?)</name>',str(a)):
        name.append() 
    for content in a:
        #'element' object is not iterable
        if re.match(r'autophagosome',content):
           definition.append()
           #use dom instead of regular expression
    print(name)
    print(id)
    print(definition)
"""
#---------main script-------------
#collectchildrenGoIDSER(GOID,resultSet)
def children_id(GOID):
    count=0
    res=data.getElementByTagName("is_a")
    for e in res:
        count=count+1
        for element in res:
             
            
            
    
            
            
        
        
        
        
    
    


                   
            
               
           
           
           
           
        
   
        
    
    
    
    
        
        
        
        
        