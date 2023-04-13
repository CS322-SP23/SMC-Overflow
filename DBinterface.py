import psycopg2


class DBInterface:

    def __init__(self, DB, username,password) -> None:
        self.conn = psycopg2.connect(host="localhost",
                                    database=DB,
                                    user=username,
                                    password=password)
        self.conn.autocommit = True


        self.cur = self.conn.cursor()

    def getVersion(self):
        return self.cur.fetchone();


    def close(self):
        self.conn.close()
        self.cur.close()
    

    def sanitizeParams(self,params):
        return params


    
    def execute(self, query,params):
        self.cur.execute(query,params)
        # self.conn.commit()











# DB = DBInterface("smc","smc_access","smc")
# print(DB.getVersion())
# DB.close()

   
