from flask import Flask,abort
from flask_script import Manager
app = Flask(__name__)
manager = Manager(app)

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return "Hello, %s" %user.name 
if __name__ == "__main__":
    app.run(debug=True)
    manager.run()