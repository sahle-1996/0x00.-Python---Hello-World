#!/usr/bin/python3
"""
Prints all City objects and their corresponding State names from the database.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Database connection
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Session creation
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to fetch City objects along with their associated State names
    cities = session.query(City).options(joinedload(City.state)).order_by(City.id).all()

    # Displaying results
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()
