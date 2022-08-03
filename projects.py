from flask import Flask,request,Blueprint,json
from flask_cors import CORS
from dbquery import projects_existing
from venv import create
from flask import Flask,request,Blueprint,json,jsonify
from flask_cors import CORS
from dbquery import projects_existing, create_project
import re

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


@projects.route("/api/projects/<id>/newproject/", methods = ['POST'])
def createProject(id):
    # receive post data as a json
    project = request.json
    projectID = id
    print(projectID)
    projectName = project['ProjectName']
    projectDescription = project['ProjectDescription']
    projectHWSets = {'hwSet1':0,'hwSet2':0}

    # Error codes for project id
    # TODO: Validation for project name??? 
    NO_ERROR = ""
    ID_ERROR_CODE_1 = "ProjectID is a not an integer"
    ID_ERROR_CODE_2 = "ProjectID Already Exists"

    apiResponse = {"Response": "Success", "IDError": NO_ERROR}

    # Validate using regex that proejct id is only numbers 
    #if not re.match("^[0-9*]+$", projectID):
        #apiResponse["Response"] = "Fail"
        #apiResponse["IDError"] = ID_ERROR_CODE_1
        # Turn project ID string into an int
    projectID = int(projectID)

    # Pass the first check
    # create a new project object
    project = create_project(projectID, projectName, projectDescription, projectHWSets)

    # check if the project is not unique
    if not (project.isProjectIDUnique(projectID)):
        # set response to fail
        apiResponse["Response"] = "Fail"
        # set id error to error code 2 - project id already exists
        apiResponse["IDError"] = ID_ERROR_CODE_2
        print('IS IT GOING HERE? IF YES WHY?')
    # create new project if passed all checks
    if (apiResponse['Response']== "Success"):
        project.createProject()
    # return api Response after all errors have been checked
    return json.dumps(apiResponse)