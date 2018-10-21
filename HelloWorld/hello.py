from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello.  This is the first step in creating the SHU Book Rental"

