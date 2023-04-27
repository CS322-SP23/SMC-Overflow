from .DBinterface import DBInterface
from .models import User


class DBManager:

    def __init__(self):
        self.interface = DBInterface("smc","smc_access","smc")
    

    
    def addQuestion(self,id,title,question,category):
        self.interface.execute("INSERT INTO user_questions (user_id, question,category,title,rating) VALUES (%s, %s,%s,%s,0)", (id,question,category,title))
        
    
    def getQuestions(self,num, category):

        self.interface.dict_cur.execute("select user_questions.*,users.username from user_questions join users on user_questions.user_id = users.user_id ORDER BY user_questions.created_at DESC LIMIT %s",(num,))
        return(self.interface.dict_cur.fetchall())

    def addUser(self,username, role,hash):
        self.interface.execute("INSERT INTO users (username,role,hash) VALUES (%s,%s,%s)", (username,role,hash))

    def deleteUser(self,user_ID):
        self.interface.execute("DELETE FROM users WHERE user_id=%s", (user_ID,))

    def deleteQuestion(self,question_ID):
        self.interface.execute("DELETE FROM user_questions WHERE question_id=%s", (question_ID,))

    # def getUserID(self,username):
        
    #     result = self.interface.cur.fetchone()
    #     return result[0] if result else None
    
    def getUser(self,user_ID=None,username=None,email=None):
        if user_ID and user_ID != "None":
            self.interface.cur.execute("SELECT * FROM users WHERE user_id=%s",(user_ID,))
        elif username:
            self.interface.cur.execute("SELECT * FROM users WHERE username=%s", (username,))
        elif email:
            self.interface.cur.execute("SELECT * FROM users WHERE username=%s", (email,))
        else:
            return None
        result = self.interface.cur.fetchone()

        if result:
            # print(result)
            return User(row=result)
        return None
        # return self.interface.cur.fetchone()

database_manager = DBManager()




if __name__== "__main__":
     DB = DBManager()
     DB.addUser("test_user","admin")
     DB.addUser("test_user2","admin")
     DB.addQuestion(1,"my questions","how are you?","math")

