from app import app, babel, get_locale
from flask import Flask, request, redirect, url_for, flash, render_template
from app.forms import ContactForm
from flask_babel import force_locale as babel_force_locale


@app.route('/')
@app.route('/index')
def index():
    return render_template('metamova.html')


@app.route('/ids')
def ids():
    with babel_force_locale('ids'):
        return render_template('metamova.html')


@app.route('/pseudo')
def pseudo():
    with babel_force_locale('pseudo'):
        return render_template('metamova.html')
