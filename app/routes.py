from app import app, mail, db
from flask import Flask, request, redirect, url_for, flash, render_template
from app.forms import ContactForm, Newsletter
from flask_babel import force_locale as babel_force_locale
from flask_mail import Message
from app.email import send
from app.models import Contact
from sqlalchemy import exc


@app.route('/')
@app.route('/index')
def index():
	form = ContactForm()
	news_form = Newsletter()
	return render_template('metamova.html', form=form, news_form=news_form)


@app.route('/ids')
def ids():
	form = ContactForm()
	news_form = Newsletter()
	with babel_force_locale('ids'):
		return render_template('metamova.html', form=form, news_form=news_form)


@app.route('/pseudo')
def pseudo():
    form = ContactForm()
    news_form = Newsletter()
    with babel_force_locale('pseudo'):
        return render_template('metamova.html', form=form, news_form=news_form)


@app.route('/uk')
def uk():
	form = ContactForm()
	news_form = Newsletter()
	with babel_force_locale('uk'):
		return render_template('metamova.html', flag_ua=True, form=form, news_form=news_form)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	news_form = Newsletter()
	if form.validate_on_submit():
		send('info@metamova.com', 'send', form=form)
		flash("Thank you! We'll get to you shortly.", "success")
		return redirect(url_for('index', _anchor='contact'))
	else:
		flash("Enter correct data.", 'danger')

	return render_template("metamova.html", form=form, news_form=news_form)


@app.route('/newsletter', methods=['GET', 'POST'])
def newsletter():
	form = ContactForm()
	news_form = Newsletter()
	if news_form.validate_on_submit():	
		try:
			user = Contact(email=news_form.news_email.data)
			db.session.add(user)
			db.session.commit()
			flash("Subscription is successful.", "primary")
			return redirect(url_for('index', _anchor='newsletter'))
		except exc.IntegrityError:
			flash("That email is already subscribe.", "danger")
			return redirect(url_for('index', _anchor='newsletter'))
	
	return render_template("metamova.html", form=form, news_form=news_form)
