
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:31:21 2019

@author: Jessi
"""
import re
input=open('address_information.csv','r')
a=input.read()
print(a)
d=re.split('\n',a)
#print(d)

#i=1
#for i in range (0,5):
#    data=re.split (',',d[i])
#    print(data)
#    name=[]
    
emails=[]
address=re.findall(r',(\S+@\S+),',a)
print(address)
#for lines in data:  
for v in address:
#match start from the opening, to find the mail address with '.com'
#it is used to test true or false, but if you store the function in a variable, its value is right or wrong
    if re.match(r'.*com.*',v):
       print(v,":correct address!")
       emails.append(v)#append address
       print()
    else:
        print(v,":wrong address!")
#!!!to verify whether something conforms to a regular expression, you need to input the thing itself, rather than the list it is in 
     
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
server = smtplib.SMTP('smtp.zju.edu.cn',25) 
mail_host="smtp.zju.edu.cn"  #设置服务器
mail_user="3180111435"    # 用户名
mail_pass="abc123456" #口令
sender = '3180111435@zju.edu.cn' 
filex=open('body.txt','r')
txt=filex.read()#to get the content
filex.close()
name=['Anna','Mary','Emma']
i=0
for item in emails:
    receivers = item  # receiver address in list emails[]
    c=name[i]
    i=i+1        
    result=re.sub('user',c,txt)#to replace user with the name of receiver respectively
    message = MIMEText( result, 'plain', 'utf-8')
    message['From'] = Header("3180111435", 'utf-8')
    message['To'] =  Header(result, 'utf-8')
    subject = "To" + str(c) + "Your analysis job has been finished!"
    message['Subject'] = Header(subject, 'utf-8')
  
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)    
        smtpObj.login("3180111435","Zhao5210")  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("Mail sent successfully")
    except smtplib.SMTPException:
        print ("Error: Fail delivery")
    
        
        
        
        
# if it has restriction message, it is because you need to verify on the Internet
#as the the email sent is too much, out of the range
#if you want, you change another account
        #760549092@qq.com     Password: Zhao5210J
    
       
    
    
   

      
      
      
