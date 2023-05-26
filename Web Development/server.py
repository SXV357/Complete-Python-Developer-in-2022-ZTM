from flask import Flask

app = Flask(__name__) # __name__ = "__main__"
# To run: export FLASK_APP = server.py | flask run
# To turn on debug mode: flask --app server run --debug

@app.route("/") # decorator which provides abstraction
def hello_world():
    '''
    Returns server body in response to a change in the base route
    '''
    return "Je m'appelle Shreyas et j'ai dix-huit ans."