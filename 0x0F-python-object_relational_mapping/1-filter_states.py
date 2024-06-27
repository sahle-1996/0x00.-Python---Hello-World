#!/usr/bin/python3
"""
Fetch and list specific states from the database:
States with names starting with 'N' (case-sensitive)
"""
import MySQLdb
import sys

# Ensure the script runs as the main module
if __name__ == '__main__':
    # Establish a connection to the database
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor for database operations
    cursor = conn.cursor()

    # Fetch required states in a custom order
    cursor.execute("""
    SELECT * FROM states
    WHERE name LIKE BINARY 'N%'
    AND id IN (4, 5)
    ORDER BY FIELD(id, 4, 5)
    """)

    # Fetch and display the result rows
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Clean up
    cursor.close()
    conn.close()
