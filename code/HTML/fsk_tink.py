from flask import Flask,render_template,request
from flask_script import Manager

app=Flask(__name__,template_folder="../HTML")
manager=Manager(app)

@app.route("/")
def index():
    return render_template('tinkhtml.html')

if __name__ == "__main__":
    app.run(debug=True)
    manager.run()