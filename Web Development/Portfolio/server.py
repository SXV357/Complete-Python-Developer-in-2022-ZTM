import re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    '''
    Display Home Page on initial load
    '''
    return render_template('index.html')

@app.route("/<string:file_name>.html")
def display_page(file_name: str = None):
    '''
    Dynamically determines which section to display based on URL params
    '''
    return render_template(f'{file_name}.html')

@app.route("/submit_form", methods = ['POST', 'GET'])
def display_completed():
    '''
    Processing/Display logic on contact form submit
    '''
    validation = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if request.method == 'POST':
        form_data = request.form.to_dict()
        email = form_data['email']
        if re.fullmatch(validation, email) and form_data["subject"] != "" and form_data["message"] != "":
            return render_template('thankyou.html', message = f'{email[0:email.index("@")]}')
            # return redirect('/thankyou.html') alternate way of displaying an html page in addition to render_template
    else:
        return "POST method wasn't detected."

# @app.errorhandler(TypeError)
# @app.errorhandler(ValueError)
# def handle_error():
#     '''
#     Error handling logic
#     '''
#     message = "The email is either invalid or the subject and/or the message fields are empty. Please try again"
#     return render_template('thankyou.html', message = message)
        
    
