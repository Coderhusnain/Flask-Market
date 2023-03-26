from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired,ValidationError
from market.models import User


class Registerform(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')
    username=StringField(label='User Name',validators=[Length(min=3,max=20),DataRequired()])
    email_address=StringField(label='Email',validators=[Email(),DataRequired()])
    password1=PasswordField(label='Password',validators=[Length(min=3),DataRequired()])
    password2=PasswordField(label='Confirm Password',validators=[EqualTo('password1'),DataRequired()])
    submit=SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username=StringField(label='Username',validators=[DataRequired()])
    password=PasswordField(label='Password',validators=[DataRequired()])
    submit=SubmitField(label="Signin")

class PurschaseItemForm(FlaskForm):
    submit=SubmitField(label="Purchase Item")

class SellItemForm(FlaskForm):
    submit=SubmitField(label="Sell Item")