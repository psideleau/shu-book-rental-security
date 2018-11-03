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

#user1 = User("jbucherati","password1","jab140@snet.net")  
#print(user1.showuser())
