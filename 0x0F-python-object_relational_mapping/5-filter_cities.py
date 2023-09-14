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
    statement = "SELECT c.name FROM cities AS c JOIN states AS s\
            ON s.id = c.state_id WHERE s.name = (%s) ORDER BY c.id ASC"
    cur.execute(statement, (state,))
    rows = cur.fetchall()
    cities = []
    for row in rows:
        for col in row:
            cities.append(str(col))
    print(", ".join(cities))
    cur.close()
    db.close()
