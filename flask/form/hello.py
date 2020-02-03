from flask import Flask,render_template,request,session,redirect,url_for,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap


class NameForm(FlaskForm):
    name = StringField('What is your name?!', validators=[Required()])
    submit = SubmitField('Submit')


app=Flask(__name__)
bootstrap=Bootstrap(app)

app.config['SECRET_KEY'] = 'hard to guess string'


# @app.route("/", methods=['GET','POST'])
# def index():
#     name=None
#     form=NameForm()
#     if form.validate_on_submit():
#         name=form.name.data
#         form.name.data='sreeram'
#     return render_template('form.html',form=form, name=name)
#     # return render_template('form2.html',form=form, name=name)


# THis code is for creating form by redirecting
# @app.route("/",methods=['GET','POST'])
# def index():
#     form=NameForm()
#     if form.validate_on_submit():
#         session['name']=form.name.data
#         return redirect(url_for('index'))
#     return render_template('form.html',form=form,name=session.get('name'))
# @app.route("/")
# def index():
#     return render_template("base.html")

# This code is for Forms with FlASH MESSAGES

@app.route("/",methods=['GET','POST'])
def index():
    form=NameForm()
    if form.validate_on_submit():    
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name')
        session['name']=form.name.data
        form.name.data='this is first data'
        return redirect(url_for('index'))
    return render_template('form.html',name=session.get('name'),form=form)


if __name__ == "__main__":
    app.run(debug=True)