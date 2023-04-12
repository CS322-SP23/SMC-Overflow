from flask import Flask, render_template

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