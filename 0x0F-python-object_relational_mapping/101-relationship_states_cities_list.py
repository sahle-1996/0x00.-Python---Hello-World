#!/usr/bin/python3
"""
Displays all State objects and their corresponding City objects from the database.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Establish connection to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Perform a query to fetch State objects and their cities
    results = session.query(State).options(joinedload(State.cities)).order_by(State.id, City.id)

    # Print the results
    for state in results:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()
