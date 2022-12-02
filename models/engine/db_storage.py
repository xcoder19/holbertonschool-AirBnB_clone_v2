#!/usr/bin/python3
from sqlalchemy import *


class DBStorage:
    """DB storage engine"""
    __engine = None
    __session = None
    user = "hbnb_dev"
    password = "hbnb_dev_pwd"
    host = '127.0.0.1'
    database = 'hbnb_dev_db'

    def __init__(self):
        self.__engine = create_engine(
            u = "@localhost/"
            f"mysql+pymysql://{self.user}:{self.password}u{self.database}",
            connect_args=dict(
                host='localhost'),
            pool_pre_ping=True)

    def close(self):
        self.__session.remove()
