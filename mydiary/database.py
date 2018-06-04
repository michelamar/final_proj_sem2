import sqlite3

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

def change_password(username, password):
    f = "timber.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('UPDATE users SET password="%s" WHERE username="%s";' %(password, username))
    db.commit()
    db.close()
    return True

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

