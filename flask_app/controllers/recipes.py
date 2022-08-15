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
    
@app.route("/recipes_add/")
def recipes_add():
    if "user_id" not in session:
        return redirect("/")
    return render_template("recipes_add.html",user=User.get_by_id({"user_id" : session["user_id"]}))

@app.route("/recipes_edit/<int:recipe_id>/")
def recipes_edit(recipe_id):
    if "user_id" not in session:
        return redirect("/")
    user=User.get_by_id({"user_id" : session["user_id"]})
    recipe=Recipe.get_by_id({"recipe_id": recipe_id })
    print("Z")
    print("user = ",user)
    print("recipe.date_made = ",type(recipe.date_made))
    return render_template("recipes_edit.html",user=user,recipe=recipe)

@app.route("/recipes_one/<int:recipe_id>/")
def recipes_one(recipe_id):
    if "user_id" not in session:
        return redirect("/")
    user = User.get_by_id({"user_id" : session["user_id"]})
    recipe = Recipe.get_by_id({"recipe_id" : recipe_id})
    return render_template("recipes_one.html",user=user,recipe=recipe)

def validation_failed(data):
    pass

def validation_succeeded(data):
    pass

def data_dictionary(data):
    pass

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

@app.route("/recipes_update/<int:recipe_id>/",methods=["POST"])
def recipes_update(recipe_id):
    if "user_id" not in session:
        return redirect("/")
    if not Recipe.validate(request.form):
        session["name"] : request.form["name"]
        session["description"] : request.form["description"]
        session["instructions"] : request.form["instructions"]
        session["date_made"] : request.form["date_made"]
        if "under_30" in request.form:
            session["under_30"] : request.form["under_30"]
        return redirect(f"/recipes_edit/{recipe_id}/")
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
        "instructions" : request.form["description"],
        "date_made" : request.form["date_made"],
        "under_30" : request.form["under_30"],
        "recipe_id" : recipe_id,
    }
    Recipe.update(data)
    return redirect("/recipes/")