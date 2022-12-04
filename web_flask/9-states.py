#!/usr/bin/python3
"""
flask app
"""
from flask import Flask

app = Flask(__name__)
try:
    from models import storage
    storage.all()
except ModuleNotFoundError:
    pass
