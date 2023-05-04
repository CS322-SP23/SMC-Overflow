import psycopg2
import DBinterface

conn = psycopg2.connect(database="smc",user="postgres")
conn.autocommit = True
cur = conn.cursor()

# cur.execute("CREATE DATABASE smc;")
#password is largly token, no external connections should every be allowed to the DB
cur.execute("CREATE USER smc_access WITH PASSWORD 'smc';") 
cur.execute("GRANT ALL PRIVILEGES ON DATABASE smc TO smc_access;")

cur.close()
conn.close()


conn = psycopg2.connect(host="localhost",database="smc",user="smc_access",password="smc")
conn.autocommit = True
cur = conn.cursor()


cur.execute("""
CREATE TABLE user_questions (
  question_id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL,
  question TEXT NOT NULL,
  rating INTEGER NOT NULL,
  category VARCHAR(255),
  title VARCHAR(255),
  created_at TIMESTAMP DEFAULT NOW()
);
""")



cur.execute("""
CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  date_created TIMESTAMP DEFAULT NOW(),
  role VARCHAR(255) NOT NULL,
  email VARCHAR(255),
  last_login TIMESTAMP,
  hash VARCHAR(150)
);
""")

cur.execute("""
CREATE TABLE user_votes (
  user_id INTEGER,
  question_id INTEGER,
  vote BIT,
  PRIMARY KEY(question_id, user_id)
);
""")

cur.close()
conn.close()
