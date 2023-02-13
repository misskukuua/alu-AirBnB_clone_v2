#!/usr/bin/python3
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This class defines a user by various attributes
    email = 
    password = 
    first_name = 
    last_name = 
    """
     __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
 
