from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from wtforms.widgets import TextArea


class ContactForm(FlaskForm):
    name = StringField("", render_kw={"placeholder": "Name"}, validators=[DataRequired()])
    email = StringField("", render_kw={"placeholder": "Email"}, validators=[DataRequired(), Email()])
    message = StringField("", render_kw={"placeholder": "Type your message here"}, widget=TextArea())
    submit = SubmitField('Send')
