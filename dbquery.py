import pymongo
client = pymongo.MongoClient("mongodb+srv://pycharmers:McCombs2022@cluster-pycharmers.riszv1q.mongodb.net/?retryWrites=true&w=majority")
mydb=client['resource_management']
mycol=mydb['users']

class creds_auth(object):
    def __init__(self,username):
        self.username=username
        
    def findPass(self):
        res=mycol.find_one({"username":self.username})
        return res['password']

class creds_new(creds_auth):
    def __init__(self, username,password):
        super().__init__(username)
        self.password=password

    def create_user(self):
        user_document = {"username": self.username, "password": self.password}
        mycol.insert_one(user_document)
    
    def is_existing_user(self):
        user_found = mycol.find_one({"username":self.username})
        if (user_found):
            return True
        else:
            return False