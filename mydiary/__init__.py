from flask import Flask, render_template, request, session, redirect, url_for, flash
import sys
import os
import sqlite3
from werkzeug import secure_filename
from datetime import datetime, timedelta

app = Flask(__name__)

def make_secret_key():
    return os.urandom(32)

app.secret_key = make_secret_key()

EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

#-------------------------------database functions-----------------------------
f = "/var/www/mydiary/mydiary/timber.db"
db = sqlite3.connect(f)
c = db.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT NOT NULL);')
c.execute('CREATE TABLE IF NOT EXISTS entries (username TEXT, date NUMERIC, type NUMERIC, data TEXT);')
db.close()

#adds user to user database
#returns true if successful
def add_user(username, password):
    f = "/var/www/mydiary/mydiary/timber.db"
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
    f = "/var/www/mydiary/mydiary/timber.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('SELECT * FROM users;')
    results = c.fetchall()
    return results == []

#retrieves password with given username
def get_password(username):
    f = "/var/www/mydiary/mydiary/timber.db"
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
    f = "/var/www/mydiary/mydiary/timber.db"
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
    f = "/var/www/mydiary/mydiary/timber.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('INSERT INTO entries VALUES("%s", "%s", "%s", "%s");' %(username, date, numtype, data))
    db.commit()
    db.close()
    return True


#returns a list of the entries under a username
def get_entry(username, date, data_type):
    f = "/var/www/mydiary/mydiary/timber.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('SELECT data FROM entries WHERE username="%s" AND date="%s" AND type="%s";' %(username, date, data_type))
    results = c.fetchall()
    if results == []:
        db.close()
        return None
    else:
        db.close()
        return results

#returns true if there is an entry for a specific date
def entryexists(username, date):
    if get_entry(username, date, 0) == None and get_entry(username, date, 1) == None:
        return False
    else:
        return True
    
#returns true if user is in database
def user_exists(username):
    f = "/var/www/mydiary/mydiary/timber.db"
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

def get_pic_id():
    f = "/var/www/mydiary/mydiary/timber.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('SELECT data FROM entries WHERE type = 0')
    results = c.fetchall()
    if results == []:
        db.close()
        return 0
    else:
        pic_id = len(results)
        db.close()
        return pic_id

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

date = 0

@app.route('/input', methods = ['POST', 'GET'])
def input():
    if 'user' in session:
        if request.method == 'GET':
            global date
            date = request.args['date']
            if entryexists(session['user'], request.args['date']):
                return redirect('/entry')
            else:
                return render_template('input.html')
        else:
            global date
            date = request.form['date']
            return render_template('input.html')
    else:
        return render_template('login.html')

def file_valid(filename):
    print "filename = " + filename
    print "extention=" + filename.split('.', 1)[1]
    print EXTENSIONS
    print "what are you = " + str(filename.split('.', 1)[1])
    return (str(filename.split('.', 1)[1]) in EXTENSIONS)

def get_pic_name(filename):
    print "filename in get pic name = " + filename
    ext = filename.split('.', 1)[1]
    name = str(get_pic_id()) + '.' + ext
    print "name = " + name
    return name

def rename(pic):
    print "pic in rename = " + pic
    path = "static/img"
    files = os.listdir(path)
    base, ext = os.path.splitext(str(pic))
    source = os.path.join("./", str(pic))
    print "get pic name = " + get_pic_name(pic)
    newfile = get_pic_name(pic)
    print "newfile= " + newfile
    dest = os.path.join("./static/img", newfile)
    os.rename(source, dest)
    return newfile

@app.route('/upload', methods = ['POST', 'GET'])
def upload():
    if request.method == 'POST':
        pic = request.files['pic']
        print "pic = " + str(pic)
        print "initial file_valid= " + str(file_valid(pic.filename))
        if file_valid(pic.filename):
            picname = secure_filename(pic.filename)
            pic.save(picname)
            picname = rename(picname)
            add_entry(session['user'], date, 0, picname), 
        else:
            flash('Sorry, file not valid')
    return redirect(url_for('entry'))

@app.route('/input_backend', methods = ['POST', 'GET'])
def input_backend():
    print "in backend"
    if request.method == 'POST':
        text = request.form['textpost']
        print "text = " + text
        add_entry(session['user'], date, 1, text)
    return redirect(url_for('entry'))
 

@app.route('/entry', methods = ['POST', 'GET'])
def entry():
    if 'user' in session:
        pics = []
        posts = []
        print date
        if not get_entry(session['user'], date, 0) == None:
            pics = get_entry(session['user'], date, 0)
        if not get_entry(session['user'], date, 1) == None:
            print "pizza"
            posts = get_entry(session['user'], date, 1)
        for index in range(len(pics)):
                pics[index] = "/static/img/" + pics[index][0]
                print pics[index]
        print "pics = " + str(pics)
        input_dest = "/input?date=" + date
        return render_template('entry.html', pics = pics, posts = posts, date = date, input_dest = input_dest)
    else:
        render_template('login.html')


@app.route('/profile', methods = ['POST','GET'])
def profile():
    if 'user' in session:
        num_posts = []
        for date in get_dates():
            pics = 0
            posts = 0
            if get_entry(session['user'], date, 1) != None:
                posts = len(get_entry(session['user'], date, 1))
            if get_entry(session['user'], date, 0) != None:
                pics = len(get_entry(session['user'], date, 0))
            num_posts.append(pics + posts)
        return render_template('profile.html', num_posts = num_posts)
    else:
        render_template('login.html')

def get_dates():
    dates = [0, 0, 0, 0, 0, 0, date]
    for index in range(1, 6):
        day_ago = datetime.strftime(datetime.now() - timedelta(index), '%m%d%Y')
        dates[6 - index] = day_ago
    return dates
        
@app.route('/logout', methods = ['POST', 'GET'])
def logout():
    session.pop('user')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run()
