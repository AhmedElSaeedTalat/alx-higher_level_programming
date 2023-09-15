#!/usr/bin/python3
""" lists all State objects from the database """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    usr = sys.argv[1]
    ps = sys.argv[2]
    db = sys.argv[3]
    statement = f'mysql+mysqldb://{usr}:{ps}@localhost/{db}'
    engine = create_engine(statement, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id.asc())
    for state in states:
        print(f"{state.id}: {state.name}")
    session.commit()
    session.close()
