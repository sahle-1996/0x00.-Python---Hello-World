#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing
the letter a from the database
Using module SQLAlchemy
"""

from model_state import Base, State
from sqlalchemy import create_engine, text, inspect
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()
    Base.metadata.create_all(engine)

    # Check if the 'state' table exists
    inspector = inspect(engine)
    if not inspector.has_table('state'):
        raise Exception("Table 'state' does not exist in the database.")

    # Using raw SQL for deletion to handle complex conditions efficiently
    stmt = text("DELETE FROM state WHERE name LIKE :pattern")
    session.execute(stmt, {"pattern": '%a%'})

    # commit and close session
    session.commit()
    session.close()
