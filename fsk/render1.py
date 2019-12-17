from flask import render_template,Flask

app = Flask(__name__, template_folder='/home/rams/Desktop/code/fsk')

@app.route('/hello/<user>')
def hello_world(user):
    return render_template('hello.html', fsks=user)


if __name__ == "__main__":
    app.run(debug=True)
