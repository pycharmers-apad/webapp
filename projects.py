from flask import Flask,request,Blueprint,json
from flask_cors import CORS
from dbquery import projects_existing

projects=Blueprint('projects',__name__,static_folder='build', static_url_path='/')
cors = CORS(projects, resources={r"/api/*": {"origins": "*"}})


@projects.route('/api/projects/<id>/',methods=['GET'])
def is_exists(id):
    project_id=int(id)
    a=projects_existing(project_id)
    if a.is_exists():
        return json.dumps({'is_exists':'true'})
    else: return json.dumps({'is_exists':'false'})



@projects.route('/api/projects/<id>/existingresources/',methods=['GET'])
def get_details(id):
    project_id=int(id)
    a=projects_existing(project_id)
    if a.is_exists():
        p=a.get_usage()
    return json.dumps(p)

