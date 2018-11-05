class User:
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
    def resetpassword(self, newpassword):
        self.password = newpassword
        return self.password
#user1 = User("jbucherati","password1","jab140@snet.net")  
#print(user1.showuser())
#(user1.showpassword())
#user1.resetpassword('password2')
#print(user1.showpassword())


