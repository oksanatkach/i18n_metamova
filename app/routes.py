from app import app, mail
from flask import Flask, request, redirect, url_for, flash, render_template
from app.forms import ContactForm
from flask_babel import force_locale as babel_force_locale
from flask_mail import Message
from app.email import send


@app.route('/')
@app.route('/index')
def index():
	form = ContactForm()
	return render_template('metamova.html', form=form)


@app.route('/ids')
def ids():
	form = ContactForm()
	with babel_force_locale('ids'):
		return render_template('metamova.html', form=form)


@app.route('/pseudo')
def pseudo():
    form = ContactForm()
    with babel_force_locale('pseudo'):
        return render_template('metamova.html', form=form)


@app.route('/en')
def en():
    form = ContactForm()
    with babel_force_locale('en'):
        return render_template('metamova.html', form=form)


@app.route('/uk')
def uk():
    form = ContactForm()
    with babel_force_locale('uk'):
        return render_template('metamova.html', form=form)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	if form.validate_on_submit():
		send('info@metamova.com', 'send', form=form)

		flash("Thank you! We'll get to you shortly.", "success")
		return redirect(url_for('index', _anchor='contact'))
	else:
		flash("Enter correct data.", 'danger')

	return render_template("metamova.html", form=form)