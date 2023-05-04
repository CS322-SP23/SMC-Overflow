import psycopg2
from flask import Flask, render_template, request
from flask_login import login_user, login_required, logout_user, current_user
from .DBmanager import database_manager
from .models import User

app = Flask(__name__)

# Create a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="smc",
    user="smc_access",
    password="smc"
)

@app.route('/profile')
@login_required
def profile():
    # Get the tutor's ID from the session
    tutor_id = database_manager.getUserById(User.get_id(current_user))

    # Retrieve the list of subjects from the database for the tutor
    cur = conn.cursor()
    cur.execute('SELECT subject FROM subjects WHERE tutor_id = %s', (tutor_id,))
    subjects = [row[0] for row in cur.fetchall()]

    return render_template('profile.html', subjects=subjects)

@app.route('/add_subject', methods=['POST'])
@login_required
def add_subject():
    print("Add subject function called")
    # Get the tutor's ID from the session
    tutor_id = database_manager.getUserById(User.get_id(current_user))

    # Get the subject from the form submission
    subject = request.form['subject']

    # Print the form data to the console
    print(f'Tutor ID: {tutor_id}, Subject: {subject}')

    # Insert the subject into the database for the tutor
    cur = conn.cursor()
    cur.execute('INSERT INTO subjects (tutor_id, subject) VALUES (%s, %s)', (tutor_id, subject))
    conn.commit()

    # Redirect the user back to their profile page
    return render_template("profile_page.html")


