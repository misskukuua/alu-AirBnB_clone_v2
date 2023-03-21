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

    @property
    def cities(self):
        var = models.storage.all()
        lista = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if city[0] == 'City':
                lista.append(var[key])
        for elem in lista:
            if elem.state_id == self.id:
                result.append(elem)
        return result

    # if os.getenv("HBNB_TYPE_STORAGE") != "db":
    #     @property
    #     def cities(self):
    #         """ list of city o=instances with state id"""
    #         all_cities = list(models.storage.all(City).values())
    #         return list(filter(lambda city: (city.id == self.id), all_cities))
