# import re
from flask import flash
# from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
# from flask_bcrypt import Bcrypt
from flask_app.models import user
# import datetime
# import humanize
db = "recipes"

class Recipe:
    def __init__(self,data):
        self.xxx = data["xxx"]

