#!/usr/bin/python3
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
user = getenv('HBNB_MYSQL_USER')
password = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
database = getenv('HBNB_MYSQL_DB')
port = ""
url = "mysql+mysqldb://{}:{}@{}:{}/{}"


class DBStorage:
    """DB storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            url.format(
                user,
                password,
                host,
                port,
                database),
            pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        dict = {}

        if cls is not None:
            query_result = self.__session.query(cls).all()
            for i in query_result:
                key = "{}.{}".format(type(i).__name__, i.id)
                dict.update({key:i})
        else:

            objs = [State, City, User, Place, Review]
            
            for obj in objs:
                query_result = self.__session.query(obj)
                for i in query_result:
                    key = "{}.{}".format(type(i).__name__, i.id)
                    dict.update({key:i})
                    

        return dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
           self.__session.delete(obj)

    def reload(self):
        self.__session = Base.metadata.create_all(self.__engine)
        session_making = sessionmaker(bind=self.__engine, expire_on_commit=False)
        scoped_s = scoped_session(session_making)
        self.__session = scoped_s()

    def close(self):
        self.__session.remove()
