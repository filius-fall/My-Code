from flask import Flask,render_template,url_for,redirect,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm,LoginForm


app=Flask(__name__)
app.config['SECRET_KEY'] = '354674946436746341416r4ws64r6we4fw'


posts = [
    {
        'author':'A.Sreeram',
        'title':'Website1',
        'content':'This is my first website content',
        'date_posted':'February 20,2020', 
    },
    {
        'author':'Bruce Wayne',
        'title':'Website_1',
        'content':'This is my  second website website',
        'date_posted':'February 21,2020', 
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts , title='Home')

@app.route('/about')
def about():
    return render_template('about.html', posts=posts, title='About')


@app.route('/register',methods=['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    else:
        return render_template('register.html', title='Register', form=form)

@app.route('/login',methods=['POST','GET'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'asreeram1729@gmail.com' and form.password.data == 'password':
            flash(f'You have been logged succesfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f"Incorrect details or you haven't registered", 'danger' )
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)