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
    states = session.query(State)\
                    .filter(City.state_id == State.id)\
                    .order_by(City.id).all()
    for state in states:
        for city in state.cities:
            print(f'{city.id}: {city.name} -> {state.name}')
    session.commit()
    session.close()
