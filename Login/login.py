from flask import Flask, render_template, request,redirect,url_for,jsonify
from User import User
from User import UserRepository
import json
app = Flask(__name__)
User_repo = UserRepository()
user_list = []
user_list.append(User("jbucherati","Password1","jab140@snet.net"))
user_list.append(User("mike", "password2", "mike@shu.edu"))
user_list.append(User("abdullah", "password3", "abdullah@shu.edu"))
#user1 = User("jbucherati","password1","jab140@snet.net")
#user2 = User("Mike","password2","mike@shu.edu")

@app.route('/')
def home():
    return "Welcome to the SHU BookRental App"
 #  return jsonify({'username': user1.showuser(),'email.address': user1.showemail()})
   
@app.route('/login',methods = ['POST', "GET"])
def login():
      return render_template('login.html')
   

@app.route('/showdata', methods = ['POST', 'GET'])
def showdata():
     user_login_name = request.form['username']
     user_login_password = request.form['password']
     
     if user_login_name == user_list[0].username:
        return jsonify({'username': user_list[0].username,'email.address': user_list[0].email_address()})
     else:
        return jsonify({'Logged in User': user_login_name, 'Password': user_login_password})

@app.route('/reset',methods = ['POST','GET'])
def reset():
    return render_template('reset.html')

@app.route('/showusers', methods = ['POST', 'GET'])
def showusers():
     # User_repo = UserRepository()
      return User_repo.listusers()
    
@app.route('/usersearch', methods =['POST', 'GET'])
def usersearch():
      
      if request.method == "POST":
            user_name = request.form['system_user']
            return User_repo.search_user(user_name)
      return render_template('usersearch.html')
   
   
   
   
   
   
    #jsonify({'Username':user_list[0].username, 'Password':user_list[0].password, 'email':user_list[0].email_address })



