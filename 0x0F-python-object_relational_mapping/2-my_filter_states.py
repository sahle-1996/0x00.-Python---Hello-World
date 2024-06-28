#!/usr/bin/python3
"""
Fetches and displays all states where the name matches the provided argument.
Uses MySQLdb for database interaction.
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Connect to the MySQL database using provided credentials
    db_conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # Create a cursor to execute SQL queries
    cursor = db_conn.cursor()
    
    # Prepare the SQL query using format
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(argv[4])
    
    # Execute the query
    cursor.execute(query)
    
    # Fetch and print the results
    for row in cursor.fetchall():
        print(row)
    
    # Close the cursor and connection
    cursor.close()
    db_conn.close()
