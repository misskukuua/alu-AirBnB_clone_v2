#!/usr/bin/python3
import os
# from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """ This amenity
    Attributes:
    name = input name
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        place_amenities = relationship('Place', secondary='place_amenity')
