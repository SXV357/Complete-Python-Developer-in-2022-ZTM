import re
import csv
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
from email_validator import EmailNotValidError, validate_email
from flask import Flask, render_template, request

app = Flask(__name__)
load_dotenv()

@app.route("/")
def home():
    '''
    Display Home Page on initial load
    '''
    return render_template('index.html')

@app.route("/<string:file_name>")
def display_page(file_name: str = None):
    '''
    Dynamically determines which section to display based on URL params
    '''
    return render_template(f'{file_name}')

@app.route("/Project-Pages/<string:fName>")
def display_project_page(fName: str = None):
    '''
    For dynamic project-page routing
    '''
    return render_template(f'Project-Pages/{fName}')

def send_email(sender: str, body: str, subject: str):
    '''
    Utilizes the details submitted in the contact form by the user to send an email to the portfolio creator
    '''
    email = EmailMessage()
    email['From'] = sender
    email["To"] = "shrevis2018@gmail.com"
    email["Subject"] = subject
    email.set_content(f'This email originated from {sender}. Message: {body}')
    try:
        with smtplib.SMTP(host = "smtp.gmail.com", port = 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("shrevis2018@gmail.com", os.environ.get("APP_PASSWORD"))
            smtp.send_message(email)
    except smtplib.SMTPException as e:
        print("Failed to send email:", e)

def write_to_csv_file(form_data: dict):
    '''
   Takes in form data and writes it to a csv file
    '''
    with open('db.csv', mode = 'a', encoding = 'utf-8', newline='') as db:
        writer = csv.writer(db, delimiter = ',', quotechar= '"', quoting=csv.QUOTE_MINIMAL)
        email, subject, message = form_data['email'], form_data['subject'], form_data['message']
        writer.writerow([email, subject, message])

@app.route("/submit_form", methods = ['POST', 'GET'])
def display_completed():
    '''
    Processing/Display logic on contact form submit
    '''
    validation = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if request.method == 'POST':
        try:
            form_data = request.form.to_dict()
            email = form_data['email']
            if re.fullmatch(validation, email):
                try:
                    validate_email(email)
                    if form_data["subject"] != "" and form_data["message"] != "":
                        write_to_csv_file(form_data)
                        send_email(email, form_data['message'], form_data['subject'])
                        return render_template('thankyou.html', message=f'{email[0:email.index("@")]}')
                    else:
                        error = "The subject and/or the message fields are empty. Please try again."
                        return render_template('thankyou.html', message=error)
                except EmailNotValidError:
                    error = "The email address is not valid. Please try again."
                    return render_template('thankyou.html', message=error)
            else:
                error = "The email address has an invalid format. Please try again."
                return render_template('thankyou.html', message=error)
        except (ValueError, TypeError):
            error = "The email address is either invalid or the subject and/or the message fields are empty. Please try again."
            return render_template('thankyou.html', message=error)
    else:
        return "POST method wasn't detected."