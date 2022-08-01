from flask import Flask,send_from_directory,request,render_template,Blueprint,json
from flask_cors import CORS
from login import login
from signup import signup


app = Flask(__name__, static_folder='build', static_url_path='/')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.register_blueprint(login)
app.register_blueprint(signup)

@app.route('/',methods=['GET'])
def index():
    return send_from_directory(app.static_folder,'index.html')

@app.route('/signup/',methods=['GET'])
def signup():
    return send_from_directory(app.static_folder,'index.html')

@app.route('/login/',methods=['GET'])
def login():
    return send_from_directory(app.static_folder,'index.html')

@app.route('/welcome/',methods=['GET'])
def welcome():
    return send_from_directory(app.static_folder,'index.html')


if __name__=="__main__":
    app.run()