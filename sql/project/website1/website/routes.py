from flask import render_template,url_for,redirect,flash,redirect
from website import app,db,bcrypt,login_manager
from website.forms import RegistrationForm,LoginForm
from website.models import User,Post
from flask_login import login_user,current_user,logout_user





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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! Now you can Login', 'success')
        return redirect(url_for('login'))
    return render_template('register2.html', title='Register', form=form)

@app.route('/login',methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash(f"Incorrect details or you haven't registered", 'danger' )
    return render_template('login1.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

