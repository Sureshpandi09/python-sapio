import json
import sqlite3

con=sqlite3.connect('D:\\DS\\DB\\Assignments\\many2many_assignment.sqlite')
curs=con.cursor()

curs.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

json_path='D:\\DS\\assign_docs\\roster_data.json'
f=open(json_path).read()
json_list=json.loads(f)
for lst in json_list:
    name=lst[0]
    title=lst[1]
    role=lst[2]

    print((name, title,role))

    curs.execute('''INSERT OR IGNORE INTO User (name)
            VALUES ( ? )''', (name,))
    curs.execute('SELECT id FROM User WHERE name = ? ', (name,))
    user_id = curs.fetchone()[0]

    curs.execute('''INSERT OR IGNORE INTO Course (title)
            VALUES ( ? )''', (title,))
    curs.execute('SELECT id FROM Course WHERE title = ? ', (title,))
    course_id = curs.fetchone()[0]

    curs.execute('''INSERT OR REPLACE INTO Member
            (user_id, course_id, role) VALUES ( ?, ?, ? )''',
                (user_id, course_id, role))
con.commit()