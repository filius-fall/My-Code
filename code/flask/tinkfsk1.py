from flask import render_template
from flask import Flask
app = Flask(__name__, template_folder='/home/rams/Desktop/code/HTML')
@app.route('/')
def index():
    return render_template('fsk_base1.html')
if __name__ == "__main__":
    app.run(debug=True)