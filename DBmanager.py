import DBinterface

class DBManager:

    def __init__(self):
        self.interface = DBinterface.DBInterface("smc","smc_access","smc")
    

    
    def addQuestion(self,id,title,question,category):
        self.interface.execute("INSERT INTO user_questions (user_id, question,category,title,rating) VALUES (%s, %s,%s,%s,0)", (id,question,category,title))
        


    
    def getQuestions(self,num, category):

        self.interface.dict_cur.execute("SELECT * FROM user_questions ORDER BY created_at DESC LIMIT %s",(num,))
        return(self.interface.dict_cur.fetchall())
        
    

    def deleteQuestion(self,question_ID):
        pass

    def getUser(self,user_ID):
        self.interface.cur.execute("SELECT * FROM users WHERE user_id=%s",(user_ID))
        return self.interface.cur.fetchone()
        

    def addUser(self,username, role):
        self.interface.execute("INSERT INTO users (username,role) VALUES (%s,%s)", (username,role))
        

    def deleteUser(self,user_ID):
        pass

    



    










# man = DBManager()

# man.addQuestion(1,"how are you?")
# man.addQuestion(2,"are you good?")
# print(man.getQuestions(20))
    

    
        