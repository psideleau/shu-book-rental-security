from flask import jsonify

class User():
    
    def __init__(self,username,password,email_address,student_id,is_active):
        self.username = username
        self.password = password
        self.email_address = email_address
        self.student_id = student_id
        self.is_active = bool(is_active)
     
    def showuser(self):
         return self.username
    def showpassword(self):
         return self.password
    def showemail(self):
         return self.email_address
    def showid(self):
        return self.student_id
    def disable(self):
        self.is_active = False
        return


class UserRepository():
    def __init__(self):
          self.users = [User("jbucherati","Password1","jab140@snet.net", "123",True), User("mike", "password2", "mike@shu.edu","456", True), User("abdullah", "password3", "abdullah@shu.edu","789",True)]
    def listusers(self):
        print(self.users)
        self.users = tuple(self.users)
        test_list = []
        for x in range(0,3):
            test_list.append(self.users[x].username)
        print(test_list)
        
        return str(test_list)
        
       # return self.users[0].username +" "+ self.users[1].username + " " + self.users[2].username
    def search_user(self,user_search):
       
       self.user_search = user_search
       if user_search == self.users[0].username:
           return "User " + user_search + " Found"
       elif user_search == self.users[1].username:
           return "User " + user_search + " Found"
       elif user_search == self.users[2].username:
           return "User " + user_search + " Found"
    
       return user_search + "  User Not Found"
    
     def email_search(self,email_search):

       self.user_search= user_search = email_search
       if email_search == self.emails[0].useremail:
           return "Useremail " + user_search + " Found"
       elif user_search != self.users[1].useremail:
           return "Useremail" + user_search + " Not Found"
       elif email_search != self.users[2].username:
           return "Useremail" + email_search + " Found"
    
    def showstudentid(self,student_ID_number):
        self.student_ID_number = student_ID_number
               
        if student_ID_number == self.users[0].student_id:
            return "Student: " + self.users[0].username + "ID " + self.users[0].student_id
        elif student_ID_number == self.users[1].student_id:
            return "Student: " + self.users[1].username + "ID " + self.users[1].student_id
        elif student_ID_number == self.users[2].student_id:
            return "Student: " + self.users[2].username + "ID " + self.users[2].student_id   
           
        return "Student not found in database."   

    def showuserstatus(self):
        #self.username = username
        account_status = []
        for x in range(0,3):
            if self.users[x].is_active == True:
                account_status.append(self.users[x].username + " Status: Active")
            elif self.users[x].is_active == False:
                account_status.append(self.users[x].username + " Status: Inactive")
        return str(account_status)
    
    def disable_user(self, username):
        self.username = username
        if username == self.users[0].username and self.users[0].is_active == True:
             User.disable(self.users[0])
             # self.users[0].is_active = False
             return "User " + self.users[0].username + " account has been disabled."
        elif username == self.users[1].username and self.users[1].is_active == True:
             User.disable(self.users[1])
             print(self.users[1].is_active)
             print(User.showuser(self.users[1]))
             return "User " + self.users[1].username + " account has been disabled."
        elif username == self.users[2].username and self.users[2].is_active == True:
             self.users[2].is_active = False
             return "User " + self.users[2].username + " account has been disabled."
        return "User Not Found or User is already disabled."
    



