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
    definition=term.getElementsByTagName('defstr')[0].childNodes[0].data
    print(type(definition))
    definitionl=[]
    idl=[]
    namel=[]
"""the three lists are created to store the information of id, definition and name respectively"""
    if re.findall(r'autophagosome',definition):
        #to make sure autophagosome is contained in the <defstr> of term 
         id=term.getElementByTagName('id')[0].childNodes[0].data
         name=term.getElementByTagName('name')[0].childNodes[0].data
    definitionl.append(definition)
    idl.append(id)
    namel.append(name)
def childnode(is_a):
    count=0
    nodelist=terms.getElementByTag("is_a")
    for nodes in nodelist:
        nodes.getChildNode("is_a")
        count+=len(nodes)
    count=count+len(nodelist)
childnode(terms)
df=pd.Datafrma(namel,columns=[name])
df=pd.Dataframe(idl,columns=[id])
df=pd.Dataframe(definitionl,columns=[definition])

"""
abandoned method
---------------------------------
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
#collectchildrenGoIDSER(GOID,resultSet)
def children_id(GOID):
    count=0
    res=data.getElementByTagName("is_a")
    for e in res:
        count=count+1
        for element in res:
"""
            
            
    
            
            
        
        
        
        
    
    


                   
            
               
           
           
           
           
        
   
        
    
    
    
    
        
        
        
        
        