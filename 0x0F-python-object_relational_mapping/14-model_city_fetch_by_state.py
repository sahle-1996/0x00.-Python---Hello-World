#!/usr/bin/python3
"""
Script to print all City objects from the database.
"""
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # Initialize engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # Initialize Session class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()
    Base.metadata.create_all(engine)

    # Query and join State and City
    results = session.query(State, City).filter(State.id == City.state_id).order_by(City.id)
    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
