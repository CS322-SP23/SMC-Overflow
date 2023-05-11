from flask import Flask, jsonify, render_template, request, send_file,redirect,url_for,escape
import json
from .DBmanager import database_manager
from flask_login import current_user, login_required
import uuid

from .auth import auth
from . import create_app

# def create_app():
#     app = Flask(__name__, static_folder="statics")
#     app.config['DEBUG'] = True
#     app.config['SECRET KEY'] = 'SFKAMSOMOENFASO3F'



#     return app

app = create_app()
# app.register_blueprint(auth)

@app.route("/index")
def hello():
    if current_user.is_authenticated:
        return render_template("index.html")
    else:
        return redirect("/login")

@app.route('/profile_page')
@login_required
def profile_page(): 
   subjects = database_manager.getTutorSubjects(current_user.user_id)
#    print(subjects)
   return render_template("profile_page.html", subjects=subjects)


@app.route('/form', methods=['GET', 'POST'])
def form():
   return render_template('form.html')

if __name__ == '__main__':
   app.run()

@app.route("/posts")
def posts():
    return render_template("posts.html")

@app.route('/data')
def get_data():
    data = database_manager.getQuestions(10,"*")
    return jsonify(data)

@app.route('/buttonPressScript')
def get_js():
    return send_file('javascript/questionSubmitButtonPress.js', mimetype='application/javascript')

# @app.route('/_subject')
# def get_js():
#     return send_file('javascript/subjectDisplayer.js', mimetype= 'text/javascript')

@app.route('/new-post', methods=['POST'])
def handle_new_post():
    data = request.form.to_dict()
    # Call the newPost function with the form data
    print(current_user.user_id)
    newPost(current_user.user_id,escape(data['title']), escape(data['content']), escape(data['category']))
    # return jsonify({'success': True})
    #return redirect("/posts")
    return redirect("/posts")


def newPost(id,title, text, category):
    database_manager.addQuestion(id,title,text,category)
    pass 


@app.route('/add_subject', methods=['GET', 'POST'])
def add_subject():
    # print(User.get_id(current_user))
    user_id = current_user.user_id
    print(database_manager.getTutorSubjects(user_id))
    subjects = database_manager.getTutorSubjects(user_id)
    if request.method == 'POST':
        # Handle form submission for adding a subject
        subject_name = request.form['subject']
        #database_manager.addSubject( user_id, subject_name, user_id, user_id)
        newSubject(current_user.user_id, subject_name)
        subjects = database_manager.getTutorSubjects(user_id) # Update list of subjects
    print(database_manager.getTutorSubjects(user_id))  # print the user's subjects
    return render_template('profile_page.html', user=current_user, subjects=subjects)

def newSubject(id, subject_name):
    database_manager.addSubject(subject_name, id) #id should be subject id 
    pass

@app.route('/delete_subject', methods=['POST'])
def delete_subject():
    user_id = current_user.user_id
    subjects = database_manager.getTutorSubjects(user_id)
    if request.method == 'POST':
        subject_name = request.form['subject_name']
        print("Subject name:", subject_name)
        subject_id = database_manager.getSubjectID(subject_name)
        database_manager.deleteSubject(user_id, subject_id)
        subjects = database_manager.getTutorSubjects(user_id) # Update list of subjects
    return redirect(url_for('profile_page', subjects=subjects))

@app.route('/increase-rating/<postID>')
def increase_rating(postID):
    rating=database_manager.submitVote(postID, current_user.user_id, 1)
    return jsonify({'rating': rating})

@app.route('/decrease-rating/<postID>')
def decrease(postID):
    rating=database_manager.submitVote(postID, current_user.user_id, 0)
    return jsonify({'rating': rating})

@app.route('/viewpost/<postID>')
def show_post(postID):
    post=database_manager.getQuestion(postID)
    return render_template("singlepost.html", post=post)

@app.route('/submit_reply/<postID>', methods=['POST'])
def reply(postID):
    text = request.form['reply_text']
    database_manager.submitReply(postID, current_user.user_id, text)
    return redirect('/viewpost/'+postID)

@app.route('/replies/<postID>')
def get_replies(postID):
    replies=database_manager.getReplies(postID)
    return jsonify(replies)