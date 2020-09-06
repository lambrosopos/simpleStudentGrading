from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])

    submit = SubmitField('Add User')


class ScoreForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired(), Length(min=5, max=50)])
    score = SelectMultipleField('Score', validators=[DataRequired()])

    submit = SubmitField('Submit')
