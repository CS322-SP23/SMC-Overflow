import DBinterface

class DBManager:

    def __init__(self):
        self.interface = DBinterface.DBInterface("smc","smc_access","smc")
    


    def addQuestion(self,id,question):
        self.interface.execute("INSERT INTO user_questions (user_id, question) VALUES (%s, %s)", (id,question))
        pass


    
    def getQuestions(self,num):

        self.interface.execute("SELECT * FROM user_questions ORDER BY created_at DESC LIMIT %s",(num,))
        return(self.interface.cur.fetchall())
        pass







man = DBManager()

man.addQuestion(1,"how are you?")
man.addQuestion(2,"are you good?")
print(man.getQuestions(20))
    

    
        