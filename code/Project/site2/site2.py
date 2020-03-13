from flask import *



app=Flask(__name__)
app.config['SECRET_KEY'] = 'filius-fall'


@app.route("/")
def home():
    res = make_response("<h4>session variable is set,<a href='/get'>Get response</a></h4>")
    session['response']='session#1'
    return res



@app.route("/get")
def getvar():
    if 'response' in session:
        s = session['response']
    return render_template('getsession.html',name=s)


if __name__ == "__main__":
    app.run(debug=True)
