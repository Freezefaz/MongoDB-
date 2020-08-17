from flask import Flask, render_template, request, redirect, url_for
import os
import flask_login
import pymongo
from dotenv import load_dotenv
# bson like JSON but in binary and only for computer
from bson.objectid import ObjectId
from passlib.hash import pbkdf2_sha256

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.environ.get('MONGO_URI')
SECRET_KEY = os.environ.get('SECRET_KEY')

# set up the secret key to flask app
app.secret_key = SECRET_KEY

# connect to the Mongo Database
client  = pymongo.MongoClient(MONGO_URI)
db = client["sample_app"]

class User(flask_login.UserMixin):
    pass

#init the flask-login for app
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.init_view = 'login'

@login_manager.user_loader
def user_loader(email):
    user = db.users.find_one({
        'email': email
    })

    # if the email exists
    if user:
        # create a user object that represents user
        user_object = User()
        user_object.id = user["email"]
        # return user_object
        return user_object
    else:
    # if the email does not exist in the database. report an error
        return None

@app.route("/")
def home():
    return render_template("home.template.html")

@app.route('/register')
def register():
    return render_template('register.template.html')

@app.route('/register', methods=["POST"])
def process_register():
    # Program Design Language
    # extract the email and password
    email = request.form.get("email")
    password = request.form.get("password")

    # todo : validation if the email and password

    # Create the new user
    db.users.insert_one({
        'email': email,
        'password': pbkdf2_sha256.hash(password)
    })

    # Redirect to the login page
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template("login.template.html")

@app.route('/login', methods=["POST"])
def process_login():

    # retrieve the email and the password from the form
    email = request.form.get("email")
    password = request.form.get("password")

    # check if the user's email exist in the database
    user = db.users.find_one({
        'email': email
    })

    # if the user exist, check if the password matches
    if user and pbkdf2_sha256.verify(password, user["password"]):
        # if the password matches, authorize the user
        user_object = User()
        user_object.id = user["email"]
        flask_login.login_user(user_object)
        # redirect to the successful login page
        return redirect(url_for("home"))

    # if login failed, return back to login page
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flask_login.logout_user()
    return redirect(url_for("login"))

@app.route("/secret")
def secret():
    return "You are in top secret area"

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)