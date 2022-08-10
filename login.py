from flask import Flask,request,Blueprint,json
from flask_cors import CORS
import encryption
import dbquery
import io

login=Blueprint('login',__name__,static_folder='build', static_url_path='/')
cors = CORS(login, resources={r"/api/*": {"origins": "*"}})

# Authenticate the user
@login.route("/api/login/auth/", methods = ["POST"])  ###Get the creds from the post request from back end
def creds_auth():                                     ###Authenticate the request and send it to front end

    my_bytes_value = request.data
    fix_bytes_value = my_bytes_value.replace(b"'", b'"')
    my_json = json.load(io.BytesIO(fix_bytes_value))  

    # encrypt the username and password
    ui_creds=encryption.encryption(my_json['username'],my_json['password'])
    #auth='nouser'
    # get the 
    server_creds=dbquery.creds_auth(ui_creds.uname_en)

    # try finding the password and return the api response successful login, wrong password, and no user in database
    try:
        db_password=server_creds.findPass()
        if db_password==ui_creds.password_en:
            auth='great success'
        else:
            auth='fail'
    except:
        print('Not Working')
        auth='nouser'
    print(auth)
    return json.dumps({'authentication':auth})

