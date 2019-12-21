from flask import Flask,redirect, url_for,render_template
app = Flask(__name__, template_folder='/home/rams/Desktop/code/HTML')

@app.route('/user/admin')
def user_admin():
    return render_template('fsk_admin.html')


@app.route('/user/<name>')
def user(name):
    return render_template('fsk_user.html', user=name) 


@app.route('/guest/<guest>')
def user_new(guest):
    if guest =='admin':
        return redirect(url_for('user_admin'))
    elif guest =='new':
        return '<h2>Hello Guest!<h2>'
    else:
        return 'Hello %s!' % guest

if __name__ == "__main__":
    app.run(debug=True)