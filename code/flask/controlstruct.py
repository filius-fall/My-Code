from flask import Flask,render_template
app = Flask(__name__, template_folder='/home/rams/Desktop/code/HTML')
@app.route('/<name>')
def new(name):
    return render_template('new.html', user = name)
if __name__ == "__main__":
    app.run(debug=True)