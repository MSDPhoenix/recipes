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
        self.date_made = data["instructions"]
        self.under_30 = data["under_30"]
        self.posted_by_id = data["posted_by_id"]
        self.posted_by = None

    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM recipes;
                """
        result = connectToMySQL(db).query_db(query)
        recipes = []
        for row in result:
            recipe = cls(row)
            user_data = {
                "user_id" : row["posted_by_id"]
            }
            recipe.posted_by = user.User.get_by_id(user_data)
            recipes.append(recipe)
        return recipes
    
    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO recipes (name,description,instructions,date_made,under_30,posted_by_id)
                VALUES (%(name)s,%(description)s,%(instructions)s,%(date_made)s,%(under_30)s,%(posted_by_id)s);
                """
        return connectToMySQL(db).query_db(query,data)

