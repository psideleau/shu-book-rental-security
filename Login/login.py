from flask import Flask, render_template, request,redirect,url_for,jsonify
from User import User
app = Flask(__name__)
user1 = User("jbucherati","password1","jab140@snet.net")
user2 = User("Mike","password2","mike@shu.edu")

@app.route('/')
def home():
   return jsonify({'username': user1.showuser(),'email.address': user1.showemail()})
   


@app.route('/login',methods = ['POST', "GET"])
def login():
  
    if request.method == 'POST':
        
        return render_template('success.html')
    return render_template('login.html')

@app.route('/showdata', methods = ['POST', 'GET'])
def showdata():
     user_login_name = request.form['username']
     user_login_password = request.form['password']
     
     if user_login_name == user2.showuser():
        return jsonify({'username': user2.showuser(),'email.address': user2.showemail()})
     else:
        return jsonify({'Logged in User': user_login_name, 'Password': user_login_password})
   
@app.route('/reset',methods = ['POST','GET'])
def reset():
    return render_template('reset.html')
   