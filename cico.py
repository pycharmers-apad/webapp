from flask import Flask,request,Blueprint,json,jsonify
from flask_cors import CORS
from dbquery import projects_existing, create_project,HWSet


cico=Blueprint('cico',__name__,static_folder='build', static_url_path='/')
cors = CORS(cico, resources={r"/api/*": {"origins": "*"}})

@cico.route('/api/projects/<id>/gethwdata/')
def getdata_hwset(id):
    hwset1=HWSet('hwSet1')
    hwset2=HWSet('hwSet2')
    op_dict={'hwset1':'hwset1','capacity_hwset1':hwset1.get_capacity(),'availability_hwset1':hwset1.get_availability(),\
    'hwset2':'hwset2','capacity_hwset2':hwset2.get_capacity(),'availability_hwset2':hwset2.get_availability()}
    return json.dumps(op_dict)



@cico.route('/api/projects/<id>/cicodata/',methods=['POST'])
def cico_hw(id):
    print(id)
    data=request.json
    wset=list(data['hwset'].keys())[0]
    qty=data['hwset'][wset]
    if(data['mode']=='checkin'):    
        hwset=HWSet(wset)
        print(int(qty))
        err_msg=hwset.check_in(int(qty))
        print(err_msg)
    if(data['mode']=='checkout'):
        hwset=HWSet(wset)
        print(int(qty))
        err_msg=hwset.check_out(int(qty))
        print(err_msg)
    return '1'