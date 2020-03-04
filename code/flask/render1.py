from flask import render_template,Flask

app = Flask(__name__, template_folder='/home/rams/Desktop/code/HTML')

@app.route('/')
def start_page():
    return render_template('image.html') 
@app.route('/hello/<user>')
def hello_world(user):
    return render_template('fsk_hello.html', fsks=user)

@app.route('/index')
def index():
    return render_template('fsk_base.html')


if __name__ == "__main__":
    app.run(debug=True)
