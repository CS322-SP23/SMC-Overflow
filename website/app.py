from flask import Flask, jsonify, render_template, request, send_file,redirect,url_for,escape
import json
from .DBmanager import database_manager
from flask_login import current_user, login_required

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
def profile_page(): 
   return render_template("profile_page.html")

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

@app.route('/increase-rating/<postID>')
def increase_rating(postID):
    database_manager.submitVote(postID, current_user.user_id, 1)
    return

@app.route('/decrease-rating/<postID>')
def decrease(postID):
    database_manager.submitVote(postID, current_user.user_id, 0)
    return