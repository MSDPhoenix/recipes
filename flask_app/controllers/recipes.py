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
    
@app.route("/create_recipe/")
def create_recipe():
    if "user_id" not in session:
        return redirect("/")
    return render_template("recipes_add.html",user=User.get_by_id({"user_id" : session["user_id"]}))

@app.route("/save_recipe/",methods=["POST"])
def save_recipe():
    if "user_id" not in session:
        return redirect("/")
    if not Recipe.validate(request.form):
        session["name"] = request.form["name"]
        session["description"] = request.form["description"]
        session["instructions"] = request.form["instructions"]
        session["date_made"] = request.form["date_made"]
        if "under_30" in request.form:
            session["under_30"] = request.form["under_30"]
        return redirect("/create_recipe/")
    if "name" in session:
        session.pop("name")
    if "description" in session:
        session.pop("description")
    if "instructions" in session:
        session.pop("instructions")
    if "date_made" in session:
        session.pop("date_made")
    if "under_30" in session:
        session.pop("under_30")
    data = {
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instructions" : request.form["instructions"],
        "date_made" : request.form["date_made"],
        "under_30" : request.form["under_30"],
        "posted_by_id" : session["user_id"],
    }
    Recipe.save(data)
    return redirect("/recipes/")