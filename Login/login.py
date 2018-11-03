from flask import Flask, render_template, request,redirect,url_for,jsonify
from User import User
app = Flask(__name__)
user1 = User("jbucherati","password1","jab140@snet.net")
@app.route('/')
def home():
   return jsonify({'username': user1.showuser(),
    'email.address': user1.showemail()})


@app.route('/login',methods = ['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
         return render_template('success.html')
    return render_template('login.html')
         