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
profile_page_backend
CREATE TABLE subjects (
  subject_id SERIAL PRIMARY KEY,
  subject_name TEXT NOT NULL
);
""")

cur.execute("""
CREATE TABLE user_subject_mapping (
  user_subject_mapping_id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(user_id),
  subject_id INTEGER NOT NULL REFERENCES subjects(subject_id),
  UNIQUE (user_id, subject_id)
);
""")

# cur.execute("""
# ALTER TABLE user_subject_mapping DROP COLUMN subject_id;
# ALTER TABLE subjects ADD COLUMN subject_id SERIAL PRIMARY KEY;
# ALTER TABLE user_subject_mapping 
#   DROP CONSTRAINT IF EXISTS user_subject_mapping_subject_id_fkey,
#   ADD CONSTRAINT user_subject_mapping_subject_id_fkey 
#     FOREIGN KEY (subject_id) REFERENCES subjects(subject_id);
# """)

cur.execute("""
CREATE TABLE user_votes (
  user_id INTEGER,
  question_id INTEGER,
  vote INTEGER,
  PRIMARY KEY(question_id, user_id)
);
""")

cur.close()
conn.close()
