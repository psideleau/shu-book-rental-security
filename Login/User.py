from flask import jsonify

class User():
    
    def __init__(self,username,password,email_address):
        self.username = username
        self.password = password
        self.email_address = email_address
     
    def showuser(self):
         return self.username
    def showpassword(self):
         return self.password
    def showemail(self):
         return self.email_address
    
#user_list = []
#user_list.append(User("jbucherati","Password1","jab140@snet.net"))
#user_list.append(User("mike", "password2", "mike@shu.edu"))
#user_list.append(User("abdullah", "password3", "abdullah@shu.edu"))

#print(user_list[1].username)


class UserRepository():
    def __init__(self):
          self.users = [User("jbucherati","Password1","jab140@snet.net"), User("mike", "password2", "mike@shu.edu"), User("abdullah", "password3", "abdullah@shu.edu")]
    def listusers(self):
        print(self.users)
        self.users = tuple(self.users)
        return self.users[0].username +" "+ self.users[1].username + " " + self.users[2].username
    def search_user(self,user_search):
       
       self.user_search = user_search
       if user_search == self.users[0].username:
           return "User " + user_search + " Found"
       elif user_search == self.users[1].username:
           return "User " + user_search + " Found"
       elif user_search == self.users[2].username:
           return "User " + user_search + " Found"
    
       return user_search + "  User Not Found"
    
        


    



