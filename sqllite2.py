import xml.etree.ElementTree as ET
import sqlite3

con=sqlite3.connect('D:\\DS\\DB\\Assignments\\track_assignment.sqlite')
curs=con.cursor()

curs.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;


CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

xml_path = 'D:\\DS\\assign_docs\\tracks\\Library.xml'
tree=ET.parse(xml_path)
tree_list=tree.findall('dict/dict/dict') # complex elements -> elements with more than one child element(tags)


def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None


for branch in tree_list:
    name = lookup(branch, 'Name')
    artist = lookup(branch, 'Artist')
    genre= lookup(branch,'Genre')
    album = lookup(branch, 'Album')
    count = lookup(branch, 'Play Count')
    rating = lookup(branch, 'Rating')
    length = lookup(branch, 'Total Time')

    if name is None or artist is None or album is None or genre is None:
        continue

    # Artist table
    curs.execute('''INSERT OR IGNORE INTO Artist (name) 
            VALUES ( ? )''', (artist,))
    curs.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = curs.fetchone()[0] # insert or ignor into => inserts value to table. If already exists ignores it.

    # Genre table
    curs.execute('''INSERT OR IGNORE INTO Genre (name) 
            VALUES ( ? )''', (genre,))
    curs.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = curs.fetchone()[0]

    # Album table
    curs.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
           VALUES ( ?, ? )''', (album, artist_id))
    curs.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = curs.fetchone()[0]

    # Track table
    curs.execute('''INSERT OR REPLACE INTO Track
         (title, album_id, genre_id, len, rating, count) 
         VALUES ( ?, ?, ?, ?, ?, ? )''',
                (name, album_id,genre_id, length, rating, count))
con.commit()
# According to the sqlite documentation, whenever the AUTOINCREMENT keyword is used after INTEGER PRIMARY KEY the "purpose of AUTOINCREMENT is to prevent the reuse of ROWIDs from previously deleted rows." There is no guarantee that the rowid's will be sequential nor that they will be incremented by 1





