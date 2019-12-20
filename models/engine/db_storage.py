#!/usr/bin/python3
"""This is the file storage class for AirBnB"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    '''
        DBStorage saves and reloads objects to and from a database
    '''

    __engine = None
    __session = None

    def __init__(self):
        '''
        connect to a database
        '''
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        connection = 'mysql+mysqldb://{}:{}@{}/{}'
        self.__engine = create_engine(connection.
                                      format(user, passwd, host, db),
                                      pool_pre_ping=True)
        ''' Deleting everything we just connected to in self.__engine'''
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
            return a dictionary of all objects if cls=None
            else a dictionary of all objects of a given class
        '''
        # all_classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
        all_classes = ['State', 'City']
        obj_dict, obj_list = {}, []
        if cls:
            all_classes = [cls]
        for each_class in all_classes:
            if type(each_class) == str:
                for obj in self.__session.query(eval(each_class)).all():
                    obj_list.append(obj)
            else:
                for obj in self.__session.query(each_class).all():
                    obj_list.append(obj)
        for obj in obj_list:
            # obj_dict[type(obj).__name__ + "." + str(obj.id)] = obj
            obj_dict["{}.{}".format(type(obj).__name__, obj.id)] = obj
        return obj_dict

    def new(self, obj):
        """Add an object to the database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit changes to the database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete objects from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all the tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
