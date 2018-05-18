from flask import Flask, render_template, request, session, redirect, url_for, flash
import sys
import os
import sqlite3   #enable control of an sqlite database

app = Flask(__name__)

#-------------------------------database functions-----------------------------
f = "timber.db"
db = sqlite3.connect(f)
c = db.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT NOT NULL);')
c.execute('CREATE TABLE IF NOT EXISTS entries (username TEXT, date NUMERIC, type NUMERIC, data TEXT);')
db.close()

#adds user to user database
#returns true if successful
def adduser(username, password):
    f = "timber.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    if empty_db():
        c.execute('INSERT INTO users VALUES("%s", "%s");' %(username, password))
        db.commit()
        db.close()
        return True
    if get_password(username) is None:
        c.execute('INSERT INTO users VALUES("%s", "%s");' %(username, password))
        db.commit()
        db.close()
        return True
    db.close()
    return False

#returns true if database is empty
def empty_db():
    f = "timber.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('SELECT * FROM users;')
    results = c.fetchall()
    return results == []

#retrieves password with given username
def get_password(username):
    f = "timber.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('SELECT password FROM users WHERE username="%s";' %(username))
    results = c.fetchall()
    if results == []:
        db.close()
        return None
    else:
        db.close()
        return results[0][0]

#changes password of user
#returns true if changed
def change_password(username, password):
    f = "timber.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('UPDATE users SET password="%s" WHERE username="%s";' %(password, username))
    db.commit()
    db.close()
    return True

#adds an entry to the database
#returns true if added
def addentry(username, date, numtype, data):
    f = "timber.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    if empty_db():
        c.execute('INSERT INTO entries VALUES("%s", "%s", "%s", "%s");' %(username, date, numtype, data))
        db.commit()
        db.close()
        return True
    if get_entry(username, date) is None:
        c.execute('INSERT INTO entries VALUES("%s", "%s", "%s", "%s");' %(username, date, numtype, data))
        db.commit()
        db.close()
        return True
    db.close()
    return False

#returns a list of the entries under a username
def getentry(username, date):
    f = "timber.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('SELECT type, data FROM entries WHERE username="%s" AND date="%s";' %(username, date))
    results = c.fetchall()
    if results == []:
        db.close()
        return None
    else:
        db.close()
        return results
    
#------------------------------------flask app--------------------------------
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
