from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy 
from functools import wraps
import sqlite3

app = Flask(__name__)

app.config['SECRET_KEY'] = 'refuge'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

# create the sqlalchemy object
db = SQLAlchemy(app)
from models import *

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f (*args, **kwargs)
		else:
			flash('You need to first Login')
			return redirect(url_for('login'))
	return wrap


@app.route('/')
def home():

	posts = db.session.query(BlogPost).all()
	# g.db = connect_db()
	# cur = g.db.execute('select * from posts')

	# posts = []
	# for row in cur.fetchall():
	# 	posts.append(dict(title=row[0], description=row[1]))
	# g.db.close()
	return render_template('index.html', posts=posts)


@app.route('/welcome', methods=['GET'])
def welcome():
	return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid credentials. Please try again.'
		else:
			session['logged_in'] = True
			flash('You are just login')
			return redirect(url_for('home'))
	return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You were just Logged out')
	return redirect(url_for('welcome'))

# def connect_db():
# 	return sqlite3.connect(app.database)


if __name__ == '__main__':
	app.run(debug=True)