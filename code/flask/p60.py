from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return "Hello, %s!" % name


if __name__ == '__main__':
    app.run(port=60,debug=True)