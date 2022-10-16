import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

email = EmailMessage()
email['from'] = 'Shreyas Viswanathan'
email['to'] = 'shrevis2018@gmail.com'
email['subject'] = 'This is a test email sent using python'

email.set_content('Hello from the Python ZTM course!')

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp :
    smtp.ehlo() # server startup message
    smtp.starttls() # encryption mechanism
    smtp.login("shrevis2018@gmail.com", "")