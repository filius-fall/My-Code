from flask import *

app = Flask(__name__)
app.secret_key='filius'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/logout")
def logout


if __name__ == "__main__":
    app.run(debug=True)