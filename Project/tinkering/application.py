from cs50 import SQL
from flask import Flask,render_template,request

app = Flask(__name__)

db = SQL("sqlite:///new.db")

@app.route('/')
def index():
    rows = db.execute('select * from registrants')
    return render_template('index.html', rows=rows)


if __name__ == "__main__":
    app.run(debug=True)