#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':
    # Make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute SQL query with user input for state name
    state_name = argv[4]
    query = "SELECT * FROM states WHERE name LIKE BINARY %s"
    cur.execute(query, (state_name,))

    # Fetch and print the result row if exists
    row = cur.fetchone()
    if row:
        print(row)

    # Clean up process
    cur.close()
    db.close()
