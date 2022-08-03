from flask import Flask,request,Blueprint,json
from flask_cors import CORS
import encryption
import dbquery
import io

login=Blueprint('login',__name__,static_folder='build', static_url_path='/')
cors = CORS(login, resources={r"/api/*": {"origins": "*"}})


@login.route("/api/login/auth/", methods = ["POST"])  ###Get the creds from the post request from back end
def creds_auth():        ###Authenticate the request and send it to front end
    
    my_bytes_value = request.data
    fix_bytes_value = my_bytes_value.replace(b"'", b'"')
    my_json = json.load(io.BytesIO(fix_bytes_value))  
    
    ui_creds=encryption.encryption(my_json['username'],my_json['password'])
    #auth='nouser'
    server_creds=dbquery.creds_auth(ui_creds.uname_en)
   
    try:
        db_password=server_creds.findPass()
        if db_password==ui_creds.password_en:
            auth='great success'
        else:
            auth='fail'
    except:
        print('not working')
        auth='nouser'
    print(auth)
    return json.dumps({'authentication':auth})

