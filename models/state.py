#!/usr/bin/python3
"""This is the state class"""
import os

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade='all, delete,delete-orphan')
    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ list of city o=instances with state id"""
            all_cities = list(models.storage.all(City).values())
            return list(filter(lambda city: (city.id == self.id), all_cities))
