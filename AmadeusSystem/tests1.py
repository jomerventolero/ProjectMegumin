import sqlite3 as s
import hashlib as hl
import os

cur_dir = __file__.rstrip('tests1.py')

print(cur_dir)
data = open(cur_dir + 'users.csv')


def create_hash(msg):
    data = hl.sha512(msg).hexdigest()
    return data
def create_database():
    con = s.connect(cur_dir + 'users.db')
    x = con.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,
                    username text NOT NULL UNIQUE,
                    password text NOT NULL);''')
    con.commit()
    con.close()

# create_database()

con = s.connect(cur_dir + 'users.db')
# con.execute('INSERT INTO users (username, password) VALUES (\'jomer287\', \'{}\');'.format(str(create_hash('junefour1999'))))

x = con.cursor()
q = x.execute('''SELECT username, password FROM users WHERE username == \'{}\' OR password == \'{}\';'''.format('jomer287', ' asdasdasdasdas'))

print x.fetchall()
q = x.fetchall()
print(type(q))

if q == [('jomer287', 'dbad9fe3a3b57f1394a7b20bae1928cb2a6777d22bff005ce8b4dc3d0fad1e02508301071607207252dff4766c732b481a0b023418d0be799e65cd95cd9ab0f8')]:
    print "Match"

con.commit()
con.close()
