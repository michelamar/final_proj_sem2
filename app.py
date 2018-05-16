from flask import Flask, render_template, request, session, redirect, url_for, flash
import sys
import os
import sqlite3   #enable control of an sqlite database

app = Flask(__name__)


@app.route('/')
def root():
    if 'user' in session:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if 'user' in session:
        return redirect(url_for('home'))
    return render_template('login.html')

def auth_login(username, password):
    return user_exists(username) and (password == get_password(username))

@app.route('/home', methods = ['POST', 'GET'])
def home():
    if 'user' not in session:
        if 'username' in request.form:
            username = request.form['username']
            password = request.form['password']
            if auth_login(username, password):
                session['user'] = username
                return render_template('calendar.html')
            else:
                flash ('Login failed. Username or password is incorrect.')
                return redirect(url_for('login'))
    else:
        return render_template('calendar.html')

@app.route('/logout', methods = ['POST', 'GET'])
def logout():
    session.pop('user')
    return redirect(url_for('login'))
        




if __name__ == '__main__':
    app.debug = True
    app.run()
