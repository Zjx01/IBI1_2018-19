# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:38:01 2019

@author: Jessi
"""
import xlrd
BLOSUM62_matrix=xlrd.open_workbook('BLOSUM62matrix.xlsx')
sheet=BLOSUM62_matrix.sheet_by_name('Sheet1')
humanseq=["humanseq","MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK"]
miceseq=["miceseq","MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK"]
randomseq=["randomseq","WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL"] 

"""
description---------------------------------------------------------------
define a function to get the difference from each sequence, and score is counted for every amino acid in the sequence
row and cols are write to get the value from BLOSUM62 chart
and the sheet is used to find the value in cell to get the final value
"""

def compare(seqa_,seqb_): 
    seqa = seqa_[1]
    seqb = seqb_[1]
    edit_distance=0 #set the initial distance =0
    sameaa=[]
    Mydict={'A':0,'R':1,'N':2,'D':3,'C':4,'Q':5,'E':6,'G':7,'H':8,'I':9,'L':10,'K':11,'M':12,'F':13,'P':14,'S':15,'T':16,'W':17,'Y':18,'V':19}
    #as columns and rows have the same arrangement for amino acid, we just need to write it once
    score=0
    alignment=""
    identityrate=0
    for i in range(len(seqa)):
        row=Mydict[seqa[i]]
        cols=Mydict[seqb[i]]#to get the location of the amino acid in the sequence
        score+=sheet.cell(row,cols).value 
        if seqa[i]!=seqb[i]:
            edit_distance+=1
        #add a score 1 if amino acids are different 
            if sheet.cell(row,cols).value>=0:#get the value from the excel according to its location
               alignment=alignment+"+"
            if sheet.cell(row,cols).value<0:
                alignment=alignment+"_"
        elif seqa[i]==seqb[i]:
            sameaa.append(seqa[i])
            alignment=alignment+seqa[i]#if amino acid is the same
            identityrate=float(len(sameaa)/len(seqa))*100
    print("edit_distance between "+seqa_[0]+ "&" +seqb_[0]+ " is", edit_distance)
    print("score=",score)
    print(alignment)
    print("for " +seqa_[0]+" & "+seqb_[0]+ ", they have the identity of",identityrate , "%")
compare(humanseq,miceseq)#compare the differences between each sequence use the function compare
compare(miceseq,randomseq)
compare(humanseq,randomseq)

"""
Bonus project:
Print out two sequences with a BLAST-like visual alignment(indicate alignment with the same amino acid 
if there is a perfect match, and print+symbol for conservative substitutions(BLOSUM>=0))
"""














           
        
    
           
           
