#!/usr/bin/python3
"""
Class definition of a City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class linked to the MySQL table `cities`.

    Attributes:
        id: An auto-generated primary key
        name: A string of 128 characters, not nullable
        state_id: An integer referencing states.id, not nullable
    """
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
