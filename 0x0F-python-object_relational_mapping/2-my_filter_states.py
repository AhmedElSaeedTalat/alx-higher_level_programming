#!/usr/bin/python3
"""
    displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument
"""
import sys
import MySQLdb


if __name__ == "__main__":
    myHost = 'localhost'
    usr = sys.argv[1]
    ps = sys.argv[2]
    myDb = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(user=usr, passwd=ps, db=myDb, host=myHost, port=3306)
    cur = db.cursor()
    statement = "SELECT * FROM states WHERE name LIKE BINARY '{}'\
            ORDER BY id ASC".format(state)
    cur.execute(statement)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
