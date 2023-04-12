from flask import Flask, jsonify, render_template, request
import json

app = Flask(__name__,static_folder="")

@app.route("/")
def hello():
    return render_template("index.html")
    
@app.route('/form', methods=['GET', 'POST'])
def form():
   return render_template('form.html')
if __name__ == '__main__':
   app.run()

@app.route("/posts")
def posts():
    return render_template("posts.html")

@app.route('/new-post', methods=['POST'])
def handle_new_post():
    data = request.form.to_dict()
    # Call the newPost function with the form data
    newPost(data['title'], data['content'], data['category'])
    return jsonify({'success': True})

def newPost(title, text, category):
     
   new_data={'title': title, 'content':text, 'category':category, 'author':"User"}
   with open('test_data/posts.json','r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
