from flask import Flask,request,Blueprint,json,jsonify
from flask_cors import CORS
from dbquery import projects_existing, create_project,HWSet

# Set the blueprint for the check in check out service
cico=Blueprint('cico',__name__,static_folder='build', static_url_path='/')
cors = CORS(cico, resources={r"/api/*": {"origins": "*"}})

'''
TODO: Implement scalable solution for when there are multiple harware sets that
      show on the check in check out view

Possible solution: Add a database function that loops through each HWSet item in MongoDB
                   and create a new HWSet object for each HWSet in MongoDB in the
                   getdata_hwset function
'''


# Gets the hw set data from the database
# TODO: Scalabilitiy update for multiple hardware sets mentioned above
@cico.route('/api/projects/<id>/gethwdata/')
def getdata_hwset(id):
    # Create the 2 HWSet objects that are connected to the HWSets in Mongo
    hwset1=HWSet('hwSet1',int(id))
    hwset2=HWSet('hwSet2',int(id))

    # Create a project object and connects that with the MongoDB Project based on 
    #   given id from the URL
    proj=projects_existing(int(id))

    # Gets the HWSet usage of the project for all HWSets
    project_name=proj.get_usage()

    # Dictionary that holds the capacity and availability of each hardware set
    op_dict={'hwset1':'hwset1','capacity_hwset1':hwset1.get_capacity(),'availability_hwset1':hwset1.get_availability(),\
    'hwset2':'hwset2','capacity_hwset2':hwset2.get_capacity(),'availability_hwset2':hwset2.get_availability(),'project_name':project_name['project_name']}
    # Return hardware set information as a json to front end
    return json.dumps(op_dict)

# Updates the given HWSet based on whether the value was checked in or checked out
# Provides an error message if you checked in or checked out too much
@cico.route('/api/projects/<id>/cicodata/',methods=['POST'])
def cico_hw(id):
    # Converts passed in json information as a dictionary
    # JSON contains the mode: Check in or Check out
    # and contains the HWSet
    data=request.json

    # Gets the HWSet objectID from the passed in HWSet
    wset=list(data['hwset'].keys())[0]

    # Quantity of resources to check in or check out
    qty=data['hwset'][wset]

    # Check qty into the hardware set into the hardware set
    # Validates in dbquery HWSet class 
    if(data['mode']=='checkin'):    
        # Creates HWSet object given the name and project id and connects object to mongo
        hwset=HWSet(wset,int(id))
        # gets api response from calling checkin function the HWSet instance
        err_msg=hwset.check_in(int(qty))
        print(err_msg)

    # Check qty out of the hardware set
    # Validates in dbquery HWSet class
    if(data['mode']=='checkout'):
        # Creates HWSet object given the name and project id and connects object to mongo
        hwset=HWSet(wset,int(id))
        # gets api response from calling checkout function on the HWSet instance
        err_msg=hwset.check_out(int(qty))
        print(err_msg)

    # return the api response set by hwset.check_in/check_out
    return json.dumps({'error_msg':err_msg})