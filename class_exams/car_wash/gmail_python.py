import smtplib 

gmailaddress = input("what is your gmail address? \n ")
gmailpassword = input("what is the password for that email address? \n  ")
mailto = input("what email address do you want to send your message to? \n ")
msg = input("What is your message? \n ")
mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
mailServer.starttls()
mailServer.login(gmailaddress , gmailpassword)
mailServer.sendmail(gmailaddress, mailto , msg)
print(" \n Sent!")
mailServer.quit()