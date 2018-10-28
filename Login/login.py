from flask import Flask, render_template, request,redirect,url_for
app = Flask(__name__)

@app.route('/')
def home():
   return "Welcome to SHU Book Rental App."

@app.route('/login',methods = ['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
         return render_template('success.html')
    return render_template('login.html')
         