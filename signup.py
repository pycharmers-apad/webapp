from dbquery import creds_new
import encryption
from flask import Flask,request,Blueprint,json
from flask_cors import CORS

signup=Blueprint('signup',__name__,static_folder='build', static_url_path='/')
cors = CORS(signup, resources={r"/api/*": {"origins": "*"}})

@signup.route("/api/signup/validate/", methods = ["POST"])
def response_validation():
    # get data from front end - json format
    request_data = request.json
    # signup response set at the beginning
    response = {"API-Signup-Response":''}
    # Get username value from json form
    uname = request_data["username"]
    passw = request_data["password"]

    creds=encryption.encryption(uname,passw)
    username,password=creds.get_encrypted_creds()

    # Username validation - Check if '!' and ' ' is not there 
    if not (username.find('!')==-1 and username.find(' ')==-1):
        print("username is not alphanumeric")
        response["API-Signup-Response"] = "Invalid username"
        return json.dumps(response)

    # Password validation - Check if '!' and ' ' is not there 
    if not (password.find('!')==-1 and password.find(' ')==-1):
        print("password is not alphanumeric")
        response["API-Signup-Response"] = "Invalid password"
        return json.dumps(response)

    new_creds=creds_new(username,password)
    # temporary code for database detection of username
    if (new_creds.is_existing_user()):
        print("user already exists")
        response["API-Signup-Response"] = "User exists"
        return json.dumps(response)
    
    # valid input 
    response["API-Signup-Response"] = "Credentials Authenticated"
    # create user in the database with credentials
    new_creds.create_user()

    return json.dumps(response)