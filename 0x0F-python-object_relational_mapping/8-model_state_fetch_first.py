#!/usr/bin/python3
"""
Script that prints the first State object from the database
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # Ensure arguments are provided correctly
    if len(argv) != 4:
        print("Usage: {} username password database_name".format(argv[0]))
        exit(1)

    # Extract arguments
    username, password, database_name = argv[1:]

    # Create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database_name), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Ensure tables are created if not exists
    Base.metadata.create_all(engine)

    # Query the first State object sorted by id
    first_state = session.query(State).order_by(State.id).first()

    # Print the result or "Nothing" if no state is found
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()
