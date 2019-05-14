# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:38:01 2019

@author: Jessi
"""
import xlrd
BLOSUM62_matrix=xlrd.open_workbook('BLOSUM62matrix.xlsx')
sheet=BLOSUM62_matrix.sheet_by_name('Sheet1')
seq1="MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK"
seq2="MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK"
seq3="WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL" 

"""
description---------------------------------------------------------------
define a function to get the difference from each sequence, and score is counted for every amino acid in the sequence
row and cols are write to get the value from BLOSUM62 chart
and the sheet is used to find the value in cell to get the final value
"""

def compare(seqa,seqb): 
    edit_distance=0 #set the initial distance =0
    Mydict={'A':0,'R':1,'N':2,'D':3,'C':4,'Q':5,'E':6,'G':7,'H':8,'I':9,'L':10,'K':11,'M':12,'F':13,'P':14,'S':15,'T':16,'W':17,'Y':18,'V':19}
    #as columns and rows have the same arrangement for amino acid, we just need to write it once
    score=0
    alignment=""
    for i in range(len(seqa)):
        row=Mydict[seqa[i]]
        cols=Mydict[seqb[i]]
        score+=sheet.cell(row,cols).value 
        if seqa[i]!=seqb[i]:
            edit_distance+=1
        #add a score 1 if amino acids are different 
            if sheet.cell(row,cols).value>=0:
               alignment=alignment+"+"
            if sheet.cell(row,cols).value<0:
                alignment=alignment+"_"
        else:
            alignment=alignment+seqa[i]
    print("edit_distance between "+seqa+"and"+seqb, edit_distance)
    print("score")
    print(alignment)
compare(seq1,seq2)
compare(seq2,seq3)
compare(seq1,seq3)

"""
Bonus project:
Print out two sequences with a BLAST-like visual alignment(indicate alignment with the same amino acid 
if there is a perfect match, and print+symbol for conservative substitutions(BLOSUM>=0))
"""














           
        
    
           
           
