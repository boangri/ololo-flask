from flask import render_template, flash, redirect, url_for
from app import app

@app.route('/')
def main():
    return render_template('index.html', title='Home')


@app.route('/services')
def services():
    return render_template('services.html', title='Services')


@app.route('/portfolio')
def portfolio():
    port = [
        {"year": 1999, "site": "http://www.xland.ru", "desc": "Some description"}
    ]
    return render_template('portfolio.html', portfolio=port)


@app.route('/contacts')
def contacts():
    return render_template('contacts.html', title='Contacts')