from pydoc import render_doc
from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt =  Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recipes/")
def recipes():
    return render_template("recipes_all.html")
    
@app.route("/register/",methods=["POST"])
def register():
    return redirect("/recipes/")

@app.route("/login/",methods=["POST"])
def login():
    return redirect("/recipes/")
