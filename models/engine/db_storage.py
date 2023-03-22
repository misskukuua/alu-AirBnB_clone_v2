#!/usr/bin/python3
""" New engine DBStorage """
import sqlalchemy
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os
from models.base_model import *

classes = {
    # 'BaseModel': BaseModel,
    'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}


class DBStorage:
    """ DBStorage Class """
    __engine = None
    __session = None

    def __init__(self):
        """ init method """
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        port = os.getenv('HBNB_MYSQL_PORT')
        env = os.getenv('HBNB_ENV')
        # storage_type = os.getenv('HBNB_STORAGE_TYPE')

        db_path = ('mysql+mysqldb://{}:{}@{}/{}'
                   .format(user, passwd, host, db))

        self.__engine = create_engine(db_path, pool_pre_ping=True)
        # drop all tables if the environment variable HBNB_ENV is equal to test
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

        # self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
        #     os.getenv('HBNB_MYSQL_USER'),
        #     os.getenv('HBNB_MYSQL_PWD'),
        #     os.getenv('HBNB_MYSQL_HOST'),
        #     os.getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)
        #
        # if os.getenv('HBNB_ENV') == "test":
        #     Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ all method """
        dict_objs = {}
        if cls:
            for name in classes:
                if cls.__name__ == name:
                    find = self.__session.query(classes[name]).all()
                    for i in find:
                        key = i.__class__.__name__ + '.' + i.id
                        dict_objs[key] = i
        elif cls is None:
            for name in classes:
                find = self.__session.query(classes[name]).all()
                for i in find:
                    key = i.__class__.__name__ + '.' + i.id
                    dict_objs[key] = i
        return dict_objs

    def new(self, obj):
        """ new method """
        self.__session.add(obj)

    def save(self):
        """ save method """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete method """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self, remove=False):
        """ reload method """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        session = scoped_session(session_factory)
        self.__session = session()

    def close(self):
        """ close method """
        self.reload.close()
