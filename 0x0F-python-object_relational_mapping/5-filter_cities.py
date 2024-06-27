#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists
all cities of that state, using the database
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute the SQL query with safe parameter substitution
    cur.execute("SELECT cities.id, cities.name FROM cities "
                "INNER JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s "
                "ORDER BY cities.id ASC", [argv[4]])

    # Fetch all rows from the query result
    rows = cur.fetchall()

    # Extract city names and join them with ", " separator
    city_names = ", ".join(row[1] for row in rows)

    # Print the formatted output as required
    print(city_names)

    # Clean up process
    cur.close()
    db.close()
