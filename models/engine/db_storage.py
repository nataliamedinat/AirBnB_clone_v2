#!/usr/bin/python3
""" Class for DBStorage """
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from os import getenv

Class DBStorage:
    """ Class for the database storage
        Class attributes:
        engine : Set to None
        session: Set to None
    """
    __engine: None
    __session: None

    def __init__(self):
        """ Instance of DBStorage class """
    self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
        getenv("HBNB_MYSQL_USER"),
        getenv("HBNB_MYSQL_PWD"),
        getenv("HBNB_MYSQL_HOST"),
        getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)



("mysql+mysqldb://HBNB_MYSQL_USER:HBNB_MYSQL_PWD@HBNB_MYSQL_HOST/HBNB_MYSQL_DB", pool_pre_ping=True) 
