
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
# from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
from .DBmanager import database_manager
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = database_manager.getUser(email=email)
        if user:
            if check_password_hash(user.hash, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                print("log in done")
                return redirect('/')
            else:
                print("bad login")
                flash('Incorrect password, try again.', category='error')
        else:
            print("invalid email")
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        #username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        print("here1")
        user = database_manager.getUser(email=email)
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')

        # elif len(username) < 4:
        #     flash('Username must be greater than 3 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        # elif len(password1) < 4:
        #     flash('Password must be at least 4 characters.', category='error')
        else:
            print("here2")

            new_user = User()
            new_user.email = email
            new_user.username="not set"
            new_user.hash =generate_password_hash(password1, method='sha256')

            print(len(new_user.hash))

            # new_user = User(email=email, username = username, password=generate_password_hash(password1, method='sha256')) #DELETE new_user ABOVE!
            database_manager.addUser(email,"user",generate_password_hash(password1, method='sha256'))

            # db.session.add(new_user)
            # db.session.commit()
            login_user(new_user, remember=True)
            # flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
    

@auth.route('/form', methods=['GET', 'POST'])
def form():
   return render_template('form.html')

@auth.route("/posts")
def posts():
    return render_template("posts.html")

@auth.route('/profile_page', methods=['GET', 'POST'])
@login_required
def profile_page():
       subjects = database_manager.getTutorSubjects(current_user.user_id)
       print(subjects)
       return render_template('profile_page.html', subjects = subjects)

# class Authenticator():

#     def __init__(self,DB) -> None:
#         self.DB=db
#         self.session_tokens={}
    




    