#!/usr/bin/python3

""" Class for DBStorage """

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from os import getenv
import json
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import sqlalchemy as db

class DBStorage:
    """ Class for the database storage
        Class attributes:
        engine : Set to None
        session: Set to None
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Instance of DBStorage class """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                       getenv("HBNB_MYSQL_USER"),
                                       getenv("HBNB_MYSQL_PWD"),
                                       getenv("HBNB_MYSQL_HOST"),
                                       getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Show all classes"""
        all_classes = ["State", "City", "User", "Place", "Review", "Amenity"]
        obj_dict = {}
        if cls is None:
            for class_name in all_classes:
                query = self.__session.query(eval(class_name)).all()
                for obj in query:
                    key = obj.__class__.__name__ + '.' + obj.id
                    obj_dict[key] = obj
        else:
            query = self.__session.query(eval(cls)).all()
            for obj in query:
                key = obj.__class__.__name__ + '.' + obj.id
                obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """ Add the object to the current dtabase session """
        if obj:
            self.__session.add()

    def save(self):
        """ Commit all the changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
