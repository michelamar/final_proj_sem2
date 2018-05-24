from flask import Flask, render_template, request, session, redirect, url_for, flash
import sys
import os
import sqlite3
from werkzeug import secure_filename

app = Flask(__name__)

def make_secret_key():
    return os.urandom(32)

app.secret_key = make_secret_key()

EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

#-------------------------------database functions-----------------------------
f = "timber.db"
db = sqlite3.connect(f)
c = db.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT NOT NULL);')
c.execute('CREATE TABLE IF NOT EXISTS entries (username TEXT, date NUMERIC, type NUMERIC, data TEXT);')
db.close()

#adds user to user database
#returns true if successful
def add_user(username, password):
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

#returns true if password is changed
def change_password(username, password):
    f = "timber.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('UPDATE users SET password="%s" WHERE username="%s";' %(password, username))
    db.commit()
    db.close()
    return True

#checks if user is in session
def loggedin():
    return 'username' in session

#adds entry to database
#returns true if entry is added
def add_entry(username, date, numtype, data):
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
def get_entry(username, date):
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

#returns true if user is in database
def user_exists(username):
    f = "timber.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('SELECT username FROM users WHERE username="%s"' %(username))
    results = c.fetchall()
    if results == []:
        db.close()
        return False
    else:
        db.close()
        return True

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

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password_verify = request.form.get('password_verify')
        if password == password_verify:
            if add_user(username, password):
                flash('Account successfully created!')
                return redirect('login')
            else:
                flash('Registration error: Username is already in use.')
        else:
            flash('Registration error: The passwords you entered do not match.')
    return render_template('create.html')

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
            return render_template('login.html')
    else:
        return render_template('calendar.html')

@app.route('/input', methods = ['POST', 'GET'])
def input():
    if 'user' in session:
        return render_template('input.html')
    else:
        render_template('login.html')

def file_valid(filename):
    return ('.' in filename) and (filename.split('.', 1)[1].lower in EXTENSIONS)

pic_id = 0

def get_pic_name(filename):
    

@app.route('/upload', methods = ['POST', 'GET'])
def upload():
    if request.method == 'POST':
        pic = request.files['image']
        if file_valid(pic.filename):
            picname = secure_filename(pic)
            pic.save(picname)
            rename(picname)
        else:
            flash('Sorry, file not valid')

def rename(filename):
    
    
@app.route('/logout', methods = ['POST', 'GET'])
def logout():
    session.pop('user')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run()
