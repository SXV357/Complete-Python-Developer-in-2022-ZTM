import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
from string import Template
from pathlib import Path # allows access to html file

load_dotenv()

pw = os.environ.get("EMAIL_PW")

index = Template(Path(r"C:\Users\14058\OneDrive\Desktop\Programming\Python Stuff\Emails\index.html").read_text()) # to read file as a string

email = EmailMessage()
email['from'] = 'Shreyas Viswanathan'
email['to'] = 'shreyasviswanathan1@gmail.com'
email['subject'] = 'This is a test email sent using python'

email.set_content(index.substitute({'name': 'Blablah'}), 'html') # will parse document accordingly and pull out body text

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp :
    smtp.ehlo() # server startup message
    smtp.starttls() # encryption mechanism
    smtp.login("shrevis2018@gmail.com", pw) # logging into account
    smtp.send_message(email)