from flask import Flask, render_template

app = Flask(__name__,static_folder="statics")

@app.route("/")
def hello():
    return render_template("index.html")
    
@app.route('/form')
def form():
   return render_template('form.html')
if __name__ == '__main__':
   app.run()
