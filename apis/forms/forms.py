from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(),Length(min=2,max=20)])
    email    = StringField('Email',
                        validators=[DataRequired(),Email()])
    # Password regular expression making sure that you add also characters and integers : 
    password =  PasswordField('Password',
                         validators=[DataRequired(),Length(min=6,max=20)])
    confirm_password =  PasswordField('Confirm Password',
                         validators=[DataRequired(),EqualTo('password')])
