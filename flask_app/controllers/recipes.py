from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/recipes/")
def recipes():
    if "user_id" not in session:
        return redirect("/")
    recipes = Recipe.get_all()
    data = {
        "user_id" : session["user_id"]
    }
    user = User.get_by_id(data)
    return render_template("recipes_all.html",recipes=recipes,user=user)
    
