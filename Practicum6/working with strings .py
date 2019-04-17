
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:31:21 2019

@author: Jessi
"""
#先用空格把每一行都分开，再把用一个list储存每一行并以逗号split开"""
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
    if re.match(r'.*com.*',v):
#if is used to test true or false, but if you store the function in a variable, its value is right or wrong
       print(v,":correct address!")
       emails.append(v)
       print()
    else:
        print(v,":wrong address!")
#!!!检验某物是否符合某种正则表达式，应输入某物。match式从第一位开始，此例中若用a为name所以均为wrong
     
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
txt=filex.read()
name=['Anna','Mary','Emma']
i=0
for item in emails:
    receivers = item  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    c=name[i]
    i=i+1        
    result=re.sub('user',c,txt)
    message = MIMEText( result, 'plain', 'utf-8')
    message['From'] = Header("3180111435", 'utf-8')
    message['To'] =  Header(result, 'utf-8')
    subject = "To" + str(c) + "Your analysis job has been finished!"
    message['Subject'] = Header(subject, 'utf-8')
  
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login("3180111435","Zhao5210")  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("Mail sent successfully")
    except smtplib.SMTPException:
        print ("Error: Fail delivery")
    #try要在循环的内部
        
        
        
        
    
    
       
    
    
   

      
      
      
