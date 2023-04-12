from flask import Flask, render_template

app = Flask(__name__, static_folder="statics")
app.config['DEBUG'] = True

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/profile_page')
def profile_page():
   return render_template("profile_page.html")

@app.route('/form')
def form():
    return render_template('form.html')

if __name__ == '__main__':
   app.run()
