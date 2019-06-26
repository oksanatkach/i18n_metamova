from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from wtforms.widgets import TextArea
from app.models import Contact


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    subject = StringField("Subject")
    message = StringField("Message", widget=TextArea())
    submit = SubmitField("Send")


class Newsletter(FlaskForm):
	news_email = StringField("Email", validators=[DataRequired(), Email()])

	

