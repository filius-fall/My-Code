from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

# app = Flask(__name__)

class NameForm(Form):
    name=StringField('What is Your Name?:', validators=[Required()])
    submit = SubmitField('Submit')