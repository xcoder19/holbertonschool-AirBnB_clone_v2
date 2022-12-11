#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from models.base_model import BaseModel, Base

storage_type = os.getenv('HBNB_TYPE_STORAGE')


class State(BaseModel):

    if storage_type == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if storage_type != "db":
        @property
        def cities(self):
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
