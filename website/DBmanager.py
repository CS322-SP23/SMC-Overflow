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

    def getQuestionsOrdered(self,num,category):
        self.interface.dict_cur.execute("select user_questions.*,users.username from user_questions join users on user_questions.user_id = users.user_id ORDER BY user_questions.created_at DESC LIMIT %s",(num,))
        return(self.interface.dict_cur.fetchall())
    def addUser(self,username, role,hash):
        self.interface.execute("INSERT INTO users (username,role,hash) VALUES (%s,%s,%s)", (username,role,hash))

    def deleteUser(self,user_ID):
        self.interface.execute("DELETE FROM users WHERE user_id=%s", (user_ID,))

    def getUserById(self, user_id):
        self.interface.dict_cur.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        user = self.interface.dict_cur.fetchone()
        return User(user_id=user['user_id'], username=user['username'], email=user['email'], password=user['password'])

    def deleteQuestion(self,question_ID):
        self.interface.execute("DELETE FROM user_questions WHERE question_id=%s", (question_ID,))

    # def getUserID(self,username):
        
    #     result = self.interface.cur.fetchone()
    #     return result[0] if result else None

    def addSubject(self, subject_name, user_id):
        # Check if the subject already exists in the database
        self.interface.execute("SELECT subject_id FROM subjects WHERE subject_name = %s", (subject_name,))
        result = self.interface.fetchone()
        if result is not None:
            subject_id = result[0]
        else:
            # Add the subject to the subjects table
            self.interface.execute("INSERT INTO subjects (subject_name) VALUES (%s) RETURNING subject_id", (subject_name,))
            subject_id = self.interface.fetchone()[0]
        
        # Check if the user has already added the same subject
        self.interface.execute("SELECT user_subject_mapping_id FROM user_subject_mapping WHERE user_id = %s AND subject_id = %s", (user_id, subject_id))
        result = self.interface.fetchone()
        if result is not None:
            return  # The user has already added the same subject, so do nothing
        
        # Add the user-subject mapping to the user_subject_mapping table
        self.interface.execute("INSERT INTO user_subject_mapping (user_id, subject_id) VALUES (%s, %s)", (user_id, subject_id))


    def deleteSubject(self, user_ID, subject_id):
        self.interface.execute("DELETE FROM user_subject_mapping WHERE user_id=%s AND subject_id=%s", (user_ID, subject_id))

    def getTutorSubjects(self,user_id):
        self.interface.dict_cur.execute(
            """
            SELECT subjects.subject_name 
            FROM subjects 
            JOIN user_subject_mapping 
            ON subjects.subject_id = user_subject_mapping.subject_id 
            WHERE user_subject_mapping.user_id = %s
            """, 
            (user_id,)
        )
        return [row['subject_name'] for row in self.interface.dict_cur.fetchall()]



    
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


    def load_user(user_id):
        user_row = database_manager.execute("SELECT * FROM users WHERE id=?", (user_id,)).fetchone()
        if user_row:
            user = User(user_row)
            user_subjects = [row[0] for row in database_manager.execute("SELECT subject FROM user_subjects WHERE user_id=?", (user_id,))]
            user.tutor_subjects = user_subjects
            return user
        return None


    def getVotes(self, question_ID):
        self.interface.execute("SELECT COUNT(*) FROM user_votes WHERE question_id=%s AND vote=1", (question_ID))
        upvotes=self.interface.cur.fetchone()
        self.interface.execute("SELECT COUNT(*) FROM user_votes WHERE question_id=%s AND vote=0", (question_ID))
        downvotes=self.interface.cur.fetchone()
        return upvotes[0]-downvotes[0]
    
    def hasVoted(self, question_ID, user_ID):
        self.interface.execute("SELECT vote FROM user_votes WHERE question_ID=%s AND user_id=%s", (question_ID, user_ID))
        row=self.interface.cur.fetchone()
        if row is None:
            return False
        else:
            return True
    
    def submitVote(self, question_id, user_ID, vote):
        if vote not in [0,1]:
            self.interface.execute("SELECT rating FROM user_questions WHERE question_id=%s", (question_id))
            rating=self.interface.cur.fetchone()
            return rating
        if self.hasVoted(question_id, user_ID)==False:
            self.interface.execute("INSERT INTO user_votes (question_id, user_id,vote) VALUES (%s,%s,%s)", (question_id,user_ID,vote))
        else:
            self.interface.execute("SELECT vote FROM user_votes WHERE question_ID=%s AND user_id=%s", (question_id, user_ID))
            row=self.interface.cur.fetchone()
            if row[0]==0:                                                                                                                    #Updating rating to reflect new state
                self.interface.execute("UPDATE user_questions SET rating = rating + 1 WHERE question_id=%s", (question_id))
                if vote==0:
                    self.interface.execute("DELETE FROM user_votes WHERE question_id=%s AND user_id=%s", (question_id,user_ID)) 
                    self.interface.execute("SELECT rating FROM user_questions WHERE question_id=%s", (question_id))
                    rating=self.interface.cur.fetchone()
                    return rating
            elif row[0]==1:
                self.interface.execute("UPDATE user_questions SET rating = rating - 1 WHERE question_id=%s", (question_id))
                if vote==1:
                    self.interface.execute("DELETE FROM user_votes WHERE question_id=%s AND user_id=%s", (question_id,user_ID)) 
                    self.interface.execute("SELECT rating FROM user_questions WHERE question_id=%s", (question_id))
                    rating=self.interface.cur.fetchone()
                    return rating

            self.interface.execute("DELETE FROM user_votes WHERE question_id=%s AND user_id=%s", (question_id,user_ID))                     #Clearing out the old vote
            self.interface.execute("INSERT INTO user_votes (question_id, user_id,vote) VALUES (%s,%s,%s)", (question_id,user_ID,vote))      #New vote
        if vote==0:
            self.interface.execute("UPDATE user_questions SET rating = rating - 1 WHERE question_id=%s", (question_id))                     #Making rating reflect new vote
        elif vote==1:
            self.interface.execute("UPDATE user_questions SET rating = rating + 1 WHERE question_id=%s", (question_id))
        self.interface.execute("SELECT rating FROM user_questions WHERE question_id=%s", (question_id))
        rating=self.interface.cur.fetchone()
        return rating

        

database_manager = DBManager()




if __name__== "__main__":
     DB = DBManager()
     DB.addUser("test_user","admin")
     DB.addUser("test_user2","admin")
     DB.addQuestion(1,"my questions","how are you?","math")

