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
        self.id = data["id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.under_30 = data["under_30"]
        self.posted_by_id = data["posted_by_id"]

    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM recipes;
                """
        result = connectToMySQL(db).query_db(query)
        recipes = []
        for row in result:
            recipe = cls(row)
            recipes.append(recipe)
        return recipes
    


