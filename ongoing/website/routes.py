import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from website import app, db, bcrypt, mail
from website.forms import RegistrationForm, LoginForm, UpdateAccountForm, CreatePost , RequestResetForm, ResetPasswordForm
from website.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message



@app.route("/")
@app.route("/home")
def home():
    page = request.args.get('page',1,type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=10)
    return render_template('home.html', posts=posts)




@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register2.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login1.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def picture_save(picture_form):
    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(picture_form.filename)
    picture_name = random_hex + file_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_name)
    picture_form.save(picture_path)

    output_size = (200,200)
    i = Image.open(picture_form)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    return picture_name

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = picture_save(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


@app.route("/post/new",methods=['GET','POST'])
@login_required
def new_post():
    form=CreatePost()
    if form.validate_on_submit():
        post=Post(title=form.title.data,content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post has been created', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html',title='New Post',form=form,legend='Create_Post')


@app.route("/post/<int:post_id>",methods=['GET','POST'])
@login_required
def post_page(post_id):
    post=Post.query.get_or_404(post_id)
    return render_template('post.html',post=post)

@app.route("/post/<int:post_id>/update", methods=['GET','POST'])
@login_required
def update_post(post_id):
    post=Post.query.get_or_404(post_id)
    form=CreatePost()
    if post.author != current_user:
        abort(403)
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('You have been Updated!!!!!', 'success')
        return redirect(url_for('post_page',post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html',title='Update Post',legend='Update_Post',form=form,post=post)



@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your Post has benn deleted succesfully', 'success')
    return redirect(url_for('home'))


@app.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
            .order_by(Post.date_posted.desc())\
            .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link: {url_for('reset_token', token=token, _external=True)}
        

    If you did not make this request then simply ignore this email and no changes will be made.
    '''
    mail.send(msg)


@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@app.route("/reset_password/<token>", methods=['GET','POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('This is invalid token', 'danger')
        return redirect(url_for('reset_request'))
    form = ReserPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        user.password = hashed_password
        db.session.commit()
        flash('Your account has been Updated! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html',form=form)
