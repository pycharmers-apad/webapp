import pymongo
client = pymongo.MongoClient("mongodb+srv://pycharmers:McCombs2022@cluster-pycharmers.riszv1q.mongodb.net/?retryWrites=true&w=majority")
mydb=client['resource_management']
mycol=mydb['users']

class creds_db(object):
    def __init__(self,username):
        self.username=username
        
    def findPass(self):
        res=mycol.find_one({"username":self.username})
        return res['password']
    
    

    def check_existing_email(email):
        email_found = mycol.find_one({"email": email})
        if(email_found):
            return True
        else:
            return False
    
def create_user(username, password):
    user_document = {"username": username, "password": password}
    mycol.insert_one(user_document)
def check_existing_user(username):
    user_found = mycol.find_one({"username":username})
    if (user_found):
        return True
    else:
        return False