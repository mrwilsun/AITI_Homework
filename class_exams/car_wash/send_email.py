import smtplib
import config

# this method creates an smtp server and sends an email using the given parameters
def send_email(subject,message,mailto):
    try:
        server=smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS,config.PASSWORD)
        text="Subject: {}\n\n{}".format(subject,message)
        server.sendmail(config.EMAIL_ADDRESS,mailto,text)
        server.quit()
        print(f"Notification email successfuly sent to {mailto}")
    except:
        print("Email failed to send.")

