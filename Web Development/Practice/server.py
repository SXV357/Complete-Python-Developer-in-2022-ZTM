from flask import Flask, render_template, url_for

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

@app.route("/<username>/<int:member_id>") # specify exact type we want for debugging purposes
def display_name(username=None, member_id=None):
    '''
    Takes in a username and an integer ID through the URL and renders them through HTML
    '''
    # Default value specified for the username and specifying a reference for it(can be anything)
    print("Username:" + username + str(member_id))
    return render_template('index.html', firstName = username, id = member_id) # firstName will be passed in through the url and the HTML file will be rendering it through the double curly brackets


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
    print(url_for('static', filename = 'favicon.ico')) # Prints out the file path used to render the icon
    return render_template('index.html')