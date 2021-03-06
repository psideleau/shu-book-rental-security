from flask import Flask, render_template, request,redirect,url_for,jsonify
from User import User
from User import UserRepository
import json
from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)
CSRFProtect(app)
csrf = CSRFProtect(app)
csrf.init_app(app)
app.config['SECRET_KEY'] = 'This_is_a_secret.'
app.config['WTF_CSRF_SECRET_KEY'] = "This_is_another_secret."

User_repo = UserRepository()
user_list = []
user_list.append(User("jbucherati","Password1","jab140@snet.net",'123',True))
user_list.append(User("mike", "password2", "mike@shu.edu",'456',True))
user_list.append(User("abdullah", "password3", "abdullah@shu.edu",'789',True))

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

@app.route('/accountstatus')
def accountstatus():
    return User_repo.showuserstatus()

@app.route('/showusers', methods = ['POST', 'GET'])
def showusers():
     
      return User_repo.listusers()
    
@app.route('/usersearch', methods =['POST', 'GET'])
def usersearch():
      
      if request.method == "POST":
            user_name = request.form['system_user']
            return User_repo.search_user(user_name)
      return render_template('usersearch.html')

#<link href= "C:\Users\Mike\newdirectory\shu-interns\shuinterns\reset.html" rel = "sty">

   
   
@app.route('/showid', methods = ['POST', 'GET'])
def showid():
      if request.method =="POST":
            student_id = request.form['student_id']
            return User_repo.showstudentid(student_id)
      return render_template('showid.html')
            
@app.route('/acctmgmt', methods = ['POST', 'GET']) 
def acctmgmt():
      if request.method =="POST":
            system_user = request.form['system_user'] 
            token = request.form['csrf_token']
            return token +  User_repo.disable_user(system_user) 
      return render_template('acctmgmt.html') 
   
   
    #jsonify({'Username':user_list[0].username, 'Password':user_list[0].password, 'email':user_list[0].email_address })



