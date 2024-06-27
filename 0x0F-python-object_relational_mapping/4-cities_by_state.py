#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute the SQL query and fetch all results at once
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "INNER JOIN states ON cities.state_id = states.id "
                "ORDER BY cities.id ASC")
    rows = cur.fetchall()

    # Print each row in the specified format
    for row in rows:
        print(row)

    # Clean up process
    cur.close()
    db.close()
