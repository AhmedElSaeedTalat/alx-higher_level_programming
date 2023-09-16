#!/usr/bin/python3
""" script to create relationship """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from relationship_city import City
from relationship_state import State, Base


if __name__ == "__main__":
    usr = sys.argv[1]
    ps = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{usr}:{ps}@localhost/{db}',
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f'{state.id}: {state.name}')
        cities = sorted(state.cities, key=lambda city: city.id)
        for city in cities:
            print(f'\t{city.id}: {city.name}')
    session.commit()
    session.close()
