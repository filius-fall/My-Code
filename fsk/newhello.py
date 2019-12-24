from flask import Flask
from flask_script import Manager
app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return '<h1>This is my first Website!</h1>'
@app.route('/user/<name>')
def user(name):
    return "Hello, %s!" % name
if __name__ == '__main__':
    manager.run()