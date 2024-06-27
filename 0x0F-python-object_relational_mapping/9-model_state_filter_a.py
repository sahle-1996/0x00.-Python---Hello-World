#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a from the database
Using module SQLAlchemy
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # Importing specific items from model_state as required
    from model_state import Base, State
    
    # Creating an engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    
    # Creating a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Creating a session
    session = Session()
    
    # Creating tables in the database (if not already created)
    Base.metadata.create_all(engine)
    
    # Querying and fetching State objects containing the letter 'a', ordered by id
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    
    # Printing results in the specified format
    for state in states_with_a:
        print(f"{state.id}: {state.name}")
    
    # Closing the session
    session.close()
