#!/usr/bin/python3
<<<<<<< HEAD
""" new class for sqlAlchemy """
import os
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
=======
""" New engine DBStorage """
>>>>>>> 1068653fe98999493d916f4b7bfdef7864f19baa
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


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
<<<<<<< HEAD
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")
=======
        """ init method """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)
>>>>>>> 1068653fe98999493d916f4b7bfdef7864f19baa

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ all method """
        dict_objs = {}
        if cls:
<<<<<<< HEAD
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return dic
=======
            for name in classes:
                if cls.__name__ == name:
                    find = self.__session.query(classes[name]).all()
                    for i in find:
                        key = i.__class__.__name__ + '.' + i.id
                        dict_objs[key] = i
        elif (cls is None):
            for name in classes:
                find = self.__session.query(classes[name]).all()
                for i in find:
                    key = i.__class__.__name__ + '.' + i.id
                    dict_objs[key] = i
        return dict_objs
>>>>>>> 1068653fe98999493d916f4b7bfdef7864f19baa

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
<<<<<<< HEAD
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(sec)
        self.__session = session()
=======
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        if remove:
            Session.remove()
        self.__session = Session()
>>>>>>> 1068653fe98999493d916f4b7bfdef7864f19baa

    def close(self):
        """ close method """
        self.reload(remove=True)

