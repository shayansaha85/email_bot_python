import smtplib
from email.message import EmailMessage

base_email_id = 'username@gmail.com' # enter your email ID
base_email_password = '123456X' # enter your password
rcv_email = input('Enter reciever email : ')
print()
subject = input('Enter the subject : ')
print()
print('Enter your message below : ')
email_msg = input()
print()


server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(base_email_id,base_email_password)
email = EmailMessage()
email['From'] = base_email_id
email['To'] = rcv_email
email['Subject'] = subject
email.set_content(email_msg)
server.send_message(email)
print()
print('Email successfully sent')
input()

