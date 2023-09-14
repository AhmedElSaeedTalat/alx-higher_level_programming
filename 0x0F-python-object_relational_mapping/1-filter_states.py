#!/usr/bin/python3
""" lists all states with a name starting with N """
import sys
import MySQLdb


if __name__ == "__main__":
    usr = sys.argv[1]
    ps = sys.argv[2]
    myDb = sys.argv[3]
    myHost = 'localhost'
    db = MySQLdb.connect(host=myHost, user=usr, passwd=ps, db=myDb, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'n%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        tuples = tuple(str(col) for col in row)
        print(tuples)
    cur.close()
    db.close()
