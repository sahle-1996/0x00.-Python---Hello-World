#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
but safe from MySQL injections!
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Establish a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Define the SQL query with parameterization to prevent SQL injection
    state_name = argv[4]
    sql_query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cur.execute(sql_query, (state_name,))

    # Fetch and print the first row only (assuming only one result is expected)
    row = cur.fetchone()
    if row:
        print(row)

    # Clean up process
    cur.close()
    db.close()
