#!/usr/bin/python3
""" connect to db and display table """


import sys
import MySQLdb
if __name__ == "__main__":
    usr = sys.argv[1]
    ps = sys.argv[2]
    my_db = sys.argv[3]
    myHost = 'localhost'
    db = MySQLdb.connect(host=myHost, user=usr, passwd=ps, db=my_db, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        info_tuple = tuple(str(col) for col in row)
        print(info_tuple)
    cur.close()
    db.close()
