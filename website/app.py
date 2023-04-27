from flask import Flask, jsonify, render_template, request, send_file
import json
import DBmanager

database_manager = DBmanager.DBManager()

def create_app():
    app = Flask(__name__, static_folder="statics")
    app.config['DEBUG'] = True
    app.config['SECRET KEY'] = 'SFKAMSOMOENFASO3F'
    return app

app = create_app()

@app.route("/")
def hello():
    return render_template("index.html")

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
    newPost(data['title'], data['content'], data['category'])
    return jsonify({'success': True})

def newPost(title, text, category):
    database_manager.addQuestion(1,title,text,category)
    pass 
