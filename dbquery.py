import pymongo
client = pymongo.MongoClient("mongodb+srv://pycharmers:McCombs2022@cluster-pycharmers.riszv1q.mongodb.net/?retryWrites=true&w=majority")
mydb=client['resource_management']

class creds_auth(object):
    def __init__(self,username):
        self.username=username
        self.mycol=mydb['users']

    def findPass(self):
        res=self.mycol.find_one({"username":self.username})
        return res['password']

class creds_new(creds_auth):
    def __init__(self, username,password):
        super().__init__(username)
        self.password=password

    def create_user(self):
        user_document = {"username": self.username, "password": self.password}
        self.mycol.insert_one(user_document)
    
    def is_existing_user(self):
        user_found = self.mycol.find_one({"username":self.username})
        if (user_found):
            return True
        else:
            return False

class projects_existing(object):
    def __init__(self,projectid):
        self.__project_id=projectid
        self.mycol=mydb['projects']
        self.hwsets=mydb['hardware_sets']

    def is_exists(self):
        project_found = self.mycol.find_one({"project_id":int(self.__project_id)})
        if(project_found):
            return True
        else:
            return False
    
    def get_usage(self):
        project_details=self.mycol.find_one({"project_id":self.__project_id},{'_id':0})
        capacity_hwsets={}
        hwsets=self.hwsets.find()
        for i in hwsets:
            capacity_hwsets.update({i['hw_set_name']:i['total_capacity']})
        project_details.update({'capacity':capacity_hwsets})
        return project_details

class checkin_checkout(object):
    pass