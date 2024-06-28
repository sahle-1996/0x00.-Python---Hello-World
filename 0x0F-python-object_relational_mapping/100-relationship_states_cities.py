#!/usr/bin/python3
"""
Adds the State object “California” with the City “San Francisco” to the database.
"""

if __name__ == "__main__":
    from sys import argv
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # Connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add new State and City
    cali = State(name='California', cities=[City(name='San Francisco')])
    session.add(cali)

    # Commit changes
    session.commit()
    session.close()
