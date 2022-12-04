#!/usr/bin/python3
"""
flask app
"""
from flask import Flask

app = Flask(__name__)
from models import storage
