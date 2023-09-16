#!/usr/bin/python3
"""  lists all State objects that contain the letter a """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    usr = sys.argv[1]
    ps = sys.argv[2]
    db = sys.argv[3]
    passed_state = sys.argv[4]
    engine = create_engine(f'mysql+mysqldb://{usr}:{ps}@localhost/{db}',
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State)\
                   .filter(State.name == passed_state)\
                   .first()
    if state is None:
        print('Not found')
    else:
        print(state.id)
    session.commit()
    session.close()
