from flask import Flask,url_for,render_template
from flask_bootstrap import Bootstrap,

app = Flask(__name__)
bootstrap=Bootstrap(app)
# @app.route('/')
# def index():
#     return url_for('static', filename='html/index.html', _external=True)

@app.route('/')
def index():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug=True)
