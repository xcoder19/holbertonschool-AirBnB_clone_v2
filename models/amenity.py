#!/usr/bin/python
"""Amenity"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models


class Amenity(BaseModel, Base):
    """Amenity"""
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Amenity"""
        super().__init__(*args, **kwargs)
