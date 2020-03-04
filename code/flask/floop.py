from flask import Flask,render_template
app = Flask(__name__, template_folder='/home/rams/Desktop/code/HTML')

@app.route('/rams')
def floop():
    name = [1,2,3]
    return render_template('fsk_floop.html', comments = name)

if __name__ == "__main__":
    app.run(debug=True)