from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Create User')


class PostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    body = StringField('body', validators=[DataRequired()])
    submit = SubmitField('Create post')

