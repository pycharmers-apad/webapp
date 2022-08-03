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

class create_project(object):
    # Constant variables that indicate the name of each key in the given document 
    # used when creating a new project
    # Used these constants so it is easier to modify code when switching databases
    # that might use different names for keys
    KEY1 = "project_id" 
    KEY2 = "project_name" 
    KEY3 = "project_description" 
    KEY4 = "hwSets"

    def __init__(self, projectID, projectName, projectDescription, projectHWSets):
        self.projectsCollection = mydb["projects"]
        self.HWSets = mydb["hardware_sets"]
        self.__projectID = projectID
        self.__projectName = projectName
        self.__projectDescription = projectDescription
        self.__projectHWSets = projectHWSets

    # function to check if the given input projectID is unique
    def isProjectIDUnique(self, projectID):
        # variable that finds if there is an existing project with the given id
        # use KEY1 because it correlates to ProjectID
        existingProjectID = self.projectsCollection.find_one({self.KEY1:projectID})

        # if the find_one returns None then that means the project is unique return True
        if (existingProjectID == None):
            return True
        # project exists so return false
        else:
            return False

    # Function call to create the new project in mongodb
    def createProject(self):
        # Create the dictionary in the needed format of the uploaded document
        newProject = {self.KEY1: self.__projectID, self.KEY2: self.__projectName, self.KEY3: self.__projectDescription, self.KEY4: self.__projectHWSets}

        # insert dict into db
        self.projectsCollection.insert_one(newProject)

        return "Success"