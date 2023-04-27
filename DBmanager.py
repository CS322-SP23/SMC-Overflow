import DBinterface

class DBManager:

    def __init__(self):
        self.interface = DBinterface.DBInterface("smc","smc_access","smc")
    

    
    def addQuestion(self,id,title,question,category):
        self.interface.execute("INSERT INTO user_questions (user_id, question,category,title,rating) VALUES (%s, %s,%s,%s,0)", (id,question,category,title))
        
    
    def getQuestions(self,num, category):

        self.interface.dict_cur.execute("select user_questions.*,users.username from user_questions join users on user_questions.user_id = users.user_id ORDER BY user_questions.created_at DESC LIMIT %s",(num,))
        return(self.interface.dict_cur.fetchall())

    def getUser(self,user_ID):
        self.interface.cur.execute("SELECT * FROM users WHERE user_id=%s",(user_ID))
        return self.interface.cur.fetchone()
        

    def addUser(self,username, role):
        self.interface.execute("INSERT INTO users (username,role) VALUES (%s,%s)", (username,role))

    def deleteUser(self,user_ID):
        self.interface.execute("DELETE FROM users WHERE user_id=%s", (user_ID,))

    def deleteQuestion(self,question_ID):
        self.interface.execute("DELETE FROM user_questions WHERE question_id=%s", (question_ID,))

    def getUserID(self,username):
        self.interface.cur.execute("SELECT user_id FROM users WHERE username=%s", (username,))
        result = self.interface.cur.fetchone()
        return result[0] if result else None




    







if __name__== "__main__":
     DB = DBManager()
     DB.addUser("test_user","admin")
     DB.addUser("test_user2","admin")
     DB.addQuestion(1,"my questions","how are you?","math")

