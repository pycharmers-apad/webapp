from flask import Flask,request,Blueprint,json,jsonify
from flask_cors import CORS
from dbquery import projects_existing, create_project


cico=Blueprint('cico',__name__,static_folder='build', static_url_path='/')
cors = CORS(cico, resources={r"/api/*": {"origins": "*"}})

@cico.route('/api/projects/<id>/gethwdata/')
def dn(id):
    print(id)
    return json.dumps({'hwSet1':'20'})
