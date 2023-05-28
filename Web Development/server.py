from flask import Flask, render_template

app = Flask(__name__) # __name__ = "__main__"
# Initial commands:
    # 1. ls
    # 2. source venv/Scripts/activate
    # 3. export FLASK_APP = server.py
# To turn on debug mode + run: flask --app server run --debug

@app.route("/") # decorator which provides abstraction
def hello_world():
    '''
    Returns server body in response to a change in the base route
    '''
    return "Je m'appelle Shreyas et j'ai dix-huit ans."

@app.route("/page2") # / is the root(base) route but we can specify more and how many ever routes as necessary
def display_new_info():
    '''
    Body in response to change in base route to /page2
    '''
    return "New route detected. Here are the page 2 contents."

@app.route("/template") # the html file needs to be located inside a folder called "templates" for it to be recognizable
def display_template():
    '''
    Renders an HTML file in response to the /template route
    '''
    return render_template('index.html')
