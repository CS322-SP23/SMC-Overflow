from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash('The passwords you entered did not match.', category='error')
        elif len(password1) < 7:
            flash('Your password must be longer than 6 characters.', category='error')
        else:
            flash('Account Created!', category='success')
    return render_template("sign_up.html")

@auth.route('/profile_page')
def profile_page():
   return render_template("profile_page.html")

@auth.route('/form', methods=['GET', 'POST'])
def form():
   return render_template('form.html')
