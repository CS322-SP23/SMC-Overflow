import DBinterface

class DBManager:

    def __init__(self):
        self.interface = DBinterface.DBInterface("smc","smc_access","smc")
    


    def addQuestion(self,id,title,question,category):
        self.interface.execute("INSERT INTO user_questions (user_id, question,category,title) VALUES (%s, %s,%s,%s)", (id,question,category,title))
        pass


    
    def getQuestions(self,num, category):

        self.interface.execute("SELECT * FROM user_questions where category=%s ORDER BY created_at DESC LIMIT %s",(category,num,))
        return(self.interface.cur.fetchall())
        pass
    








# man = DBManager()

# man.addQuestion(1,"how are you?")
# man.addQuestion(2,"are you good?")
# print(man.getQuestions(20))
    

    
        