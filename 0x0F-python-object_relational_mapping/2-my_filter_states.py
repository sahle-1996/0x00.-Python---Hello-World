#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Define the SQL query with user input for state name
    state_name = sys.argv[4]
    sql_query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cursor.execute(sql_query, (state_name,))

    # Fetch and print the result row if exists
    row = cursor.fetchone()
    if row:
        print(row)

    # Clean up process
    cursor.close()
    db.close()
