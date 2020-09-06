from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])

    submit = SubmitField('Add User')


class ScoreForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired(), Length(min=5, max=50)])
    score = SelectField('Score', choices=[1, 2, 3], coerce=int, validators=[DataRequired()])

    submit = SubmitField('Submit')
