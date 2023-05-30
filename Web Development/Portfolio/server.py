from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<string:file_name>.html")
def display_page(file_name: str = None):
    '''
    Dynamically determines which section to display based on URL params
    '''
    return render_template(f'{file_name}.html')
