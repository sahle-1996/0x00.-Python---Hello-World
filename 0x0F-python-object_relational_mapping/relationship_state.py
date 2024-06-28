#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
"""
    Module defining the State class, inheriting from Base.
"""

Base = declarative_base()


class State(Base):
    """
        State class linked to the 'states' table.
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
