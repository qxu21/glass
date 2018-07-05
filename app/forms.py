from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class ServerLoginForm(FlaskForm):
    password = StringField('PASSWORD', validators=[DataRequired()])
