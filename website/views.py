from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template('index.html', user=current_user)

# @views.route('/profile', methods=['GET', 'POST'])
# @login_required
# def profile():
#     if request.method == 'POST':
#         # Get the subject from the form data
#         subject = request.form['subject']

#         # Add the subject to the user's TutorSubject list
#         current_user.TutorSubject.append(subject)

#         # Update the user's data in the database
#         db.session.commit()

#     return render_template('profile.html', user=current_user)
