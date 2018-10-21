from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello.  This is the first step in creating the SHU Book Rental"

@app.route('/index')
def index():
    return render_template('index.html')
