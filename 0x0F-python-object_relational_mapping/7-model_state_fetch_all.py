#!/usr/bin/python3
"""
Script that lists all State objects from the database - Using module SQLAlchemy
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

    # Query all State objects, sorted by id ascending
    states = session.query(State).order_by(State.id).all()

    # Print results in the required format
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
