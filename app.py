from flask import Flask,send_from_directory,request,render_template,Blueprint,json
from flask_cors import CORS

# Import api py files into app.py
from login import login
from signup import signup
from projects import projects
from cico import cico

# Intiailize app with static folder set to the build folder
app = Flask(__name__, static_folder='build', static_url_path='/')

# Enable Cross Origin Request
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Add the api route calls in other python files to the register blueprint
# Connects api py files to app.py
app.register_blueprint(login)
app.register_blueprint(signup)
app.register_blueprint(projects)
app.register_blueprint(cico)

# Serve static html files as a view for the user at these routes
@app.route('/',methods=['GET'])
def index():
    return send_from_directory(app.static_folder,'index.html')

@app.route('/signup/',methods=['GET'])
def signup():
    return send_from_directory(app.static_folder,'index.html')

@app.route('/login/',methods=['GET'])
def login():
    return send_from_directory(app.static_folder,'index.html')

@app.route('/projects/',methods=['GET'])
def projects():
    return send_from_directory(app.static_folder,'index.html')

@app.route('/projects/<id>/resources/')
def resources(id):
    print(id)
    return send_from_directory(app.static_folder,'index.html')

@app.route('/projects/<id>/cico/')
def cico(id):
    print(id)
    return send_from_directory(app.static_folder,'index.html')


if __name__=="__main__":
    app.run()