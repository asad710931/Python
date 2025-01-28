

import smtplib


#send mail to single email

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("sender_email_id", "sender_email_id_password")
# message to be sent
message = "Message_you_need_to_send"
# sending the mail
s.sendmail("sender_email_id", "receiver_email_id", message)
# terminating the session
s.quit()



#send mail to multiple email

# list of email_id to send the mail
mailList = ["email1@gmail.com", "email2@gmail.com"]

for mail in mailList:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("sender_email_id", "sender_email_id_password")
    message = "Message_you_need_to_send"
    s.sendmail("sender_email_id", mail, message)
    s.quit()
