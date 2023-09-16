#!/usr/bin/python3
"""  class definition of a City """
from sqlalchemy import String, Integer, Column, ForeignKey
from relationship_state import Base, State


class City(Base):
    """ class City to set table states
        Args:
            __tablename__: table name
            id: id of rows
            name: name of states
    """
    __tablename__ = 'cities'
    id = Column(Integer,
                autoincrement=True,
                nullable=False,
                unique=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
