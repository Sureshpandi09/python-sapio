# Table => called as Relation in math.
# Columns => Fields  ........ Rows => Tuples
import sqlite3
conn=sqlite3.connect('D:\\DS\\DB\\py4e_Assignment1.sqlite') # makes connection to DB if exists, else create one.
curs=conn.cursor() # cursor -> like handle in python to run the sql queries

curs.execute('DROP TABLE IF EXISTS Counts') # drops(deletes) the entire table if exists in the name Counts
curs.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname='C:\\Users\\Sureshpandi\\OneDrive\\Desktop\\mbox.txt'
fopen=open(fname)
for line in fopen:
    if not line.startswith('From:'):
        continue
    mail=(((line.split())[1]).split('@'))[1]
    curs.execute('SELECT count FROM Counts WHERE org = ? ', (mail,))
    # ? ->is a place holder whose value will be replaced by the value in the tuple(here it is single place holder so on tuple(mail)
    row = curs.fetchone()
    # fetchall() fetches all the rows of a query result. An empty list is returned if there is no record to fetch the cursor.
    # fetchone() method returns one row or a single record at a time. It will return None if no more rows / records are available.
    if row is None:
        curs.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (mail,))
    else:
        curs.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(mail,))
conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in curs.execute(sqlstr):
    print(str(row[0]), row[1])

curs.close()

# PRAGMA table_info([<table name>]) -> sqlite query to describe table details.