#!/usr/bin/python3
""" List all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == '__main__':
    # Connect to the MySQL database
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object to interact with the database
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states")

    # Fetch and print each row from the result set
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and connection to clean up
    cursor.close()
    connection.close()
