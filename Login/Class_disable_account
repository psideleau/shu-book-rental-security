class DisableAccount():
    
    def __init__(self,username,email_address,student_id,is_active,attempt_left):
        self.username = username
        self.email_address = email_address
        self.student_id = student_id
        self.is_active = bool(is_active)
        self.attempt_left = attempt_left
        self.total_attempt = 3
        self.session_minutes = 30
     
    def showuser(self):
         return self.username
        
    def showemail(self):
         return self.email_address
    def showid(self):
        return self.student_id
    def disable(self):
        self.is_active = False
        
    def getTotalAttempt(self):
        return self.total_attempt
    
    def setAttempt(self):
         self.attempt_left =  self.attempt_left - 1
         
    def getAttemptleft(self):
        return self.attempt_left
    
    def getSessionMinutes(self):
        return self.session_minutes
    
