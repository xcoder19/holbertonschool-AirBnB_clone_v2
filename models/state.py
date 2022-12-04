#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from models.city import City
import models
from sqlalchemy import *
from sqlalchemy.orm import *
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    class State(BaseModel, Base):
        """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')
else:
    class State(BaseModel):
        name = ""

        @property
        def cities(self):
            cities_state_relationship = []
            cities = models.storage.all(City)
            for k, v in cities:
                if v.state_id == self.id:
                    cities_state_relationship.append(v)
            return cities_state_relationship
