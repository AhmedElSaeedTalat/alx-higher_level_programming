#!/usr/bin/python3
"""  lists all State objects that contain the letter a """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import Base, City
import sys


if __name__ == "__main__":
    usr = sys.argv[1]
    ps = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{usr}:{ps}@localhost/{db}',
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State)\
                    .filter(State.id == City.state_id)\
                    .all()
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.commit()
    session.close()
