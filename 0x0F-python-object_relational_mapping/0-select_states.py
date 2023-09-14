#!/usr/bin/python3
""" connect to db and display table """


import sys
import MySQLdb
usr = sys.argv[1]
pas = sys.argv[2]
my_db = sys.argv[3]
my_host = 'localhost'
db = MySQLdb.connect(host=my_host, user=usr, passwd=pas, db=my_db, port=3306)
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    info_tuple = tuple(str(col) for col in row)
    print(info_tuple)
