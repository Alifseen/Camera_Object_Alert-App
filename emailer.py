import os
import smtplib
from email.message import EmailMessage  ## Used to send attachments with emails
import imghdr

def send_email(img_path):
    ## Open mid image
    with open(img_path, "rb") as file:
        content = file.read()

    ## Setup message
    emsg = EmailMessage()
    emsg["Subject"] = "New Object Appeared"
    emsg.set_content("Hey, i think its a pokemon")
    emsg.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    ## Setup email
    username = "alifseen@gmail.com"
    password = os.getenv("EMAILSENDERPASS")
    email = smtplib.SMTP("smtp.gmail.com", 587)
    email.ehlo()
    email.starttls()
    email.login(username, password)

    ## Send email
    email.sendmail(username, username, emsg.as_string())
    email.quit()