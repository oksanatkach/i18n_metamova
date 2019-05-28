from flask import render_template
from flask_mail import Message
from threading import Thread
import os

from app import app, mail

# Async sending message
def send_async_msg(app, msg):	
	with app.app_context():
		mail.send(msg)

def send(to, template, **kwargs):	
	msg = Message(kwargs.get('form').email.data + " : " + \
					kwargs.get('form').subject.data, sender=os.environ.get('SENDER'), recipients=[to])
	msg.body = render_template(template + '.txt', **kwargs)
	
	thr = Thread(target=send_async_msg, args=(app, msg))
	thr.start()