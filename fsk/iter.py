from flask import Flask,render_template

app = Flask(__name__ , template_folder='/home/rams/Desktop/code/fsk')

@app.route('/marks')
def marks_func():
    dict = {'phy':60,'math':40,'che':80}
    return render_template('table.html', answer = dict)

if __name__ == "__main__":
    app.run(debug=True) 