#!/usr/bin/python3
"""Filter states Module."""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id;"
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        if state[1][0] == 'N':
            print(state)
    cur.close()
    db.close()
