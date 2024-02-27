import  smtplib as s

ob = s.SMTP('smtp.gmail.com',587) # 587 is a gmail port number
ob.ehlo()
ob.starttls()
username = 'prabhamaurya475@gmail.com'
password = 'kiran_pass@word'
ob.login(username,password)
subject = "tesing python"
body  = "I Love python"
message = f"subject:{subject} \n {body}"
list_add = ['shikhamaurya2021@gmai.com']

# mail sending
ob.sendmail('prabhamaurya475@gmail.com',list_add,message)
print("send mail")
ob.quit()