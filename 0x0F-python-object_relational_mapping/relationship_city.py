#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base
"""
    Module that defines the City class, inheriting from Base.
"""


class City(Base):
    """
        City class, mapping to the 'cities' table.
    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
