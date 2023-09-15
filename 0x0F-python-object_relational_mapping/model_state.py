#!/usr/bin/python3
"""  class definition of a State """
from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Integer, Column
Base = declarative_base()


class State(Base):
    """ class State to set table states
        Args:
            __tablename__: table name
            id: id of rows
            name: name of states
    """
    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement=True,
                nullable=False,
                unique=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
