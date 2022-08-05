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
        self.hwsets=mydb['hardware-sets']

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
    
    
    def check_in(self, qty, hw_set_name):
        err_code = 0
        
        #current_hwSets = ProjectDB.find_one({"project_id":self.project_id})['hwSets']
        current_hwSet_alloc = self.hwSets[hw_set_name]

        new_alloc = current_hwSet_alloc - qty

        if new_alloc < 0:
            err_code = -1
            self.hwSets[hw_set_name] = 0
            self.mycol.update_one({"project_id":self.project_id}, {"$set": {"hwSets."+str(hw_set_name):self.hwSets[hw_set_name]}})
        else:
            self.hwSets[hw_set_name] = new_alloc
            self.mycol.update_one({"project_id":self.project_id}, {"$set": {"hwSets."+str(hw_set_name):self.hwSets[hw_set_name]}})

        return err_code


    # for Project, check_out = add resources to Project
    def check_out(self, qty, hw_set_name):
        err_code = 0
        HWSetDB=mydb['hardware-sets']
        current_hwSet_alloc = self.hwSets[hw_set_name]
        current_hwSet_avail = HWSetDB.find_one({"hw_set_name":hw_set_name})["available_capacity"]
        
        if qty > current_hwSet_avail:
            err_code = -1
            self.hwSets[hw_set_name] = current_hwSet_avail
            self.mycol.update_one({"project_id":self.project_id}, {"$set": {"hwSets."+str(hw_set_name):self.hwSets[hw_set_name]}})
        else:
            self.hwSets[hw_set_name] = current_hwSet_alloc + qty
            self.mycol.update_one({"project_id":self.project_id}, {"$set": {"hwSets."+str(hw_set_name):self.hwSets[hw_set_name]}})

        return err_code

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
        print(newProject)
        # insert dict into db
        self.projectsCollection.insert_one(newProject)
        return "Success"
    
class HWSet:
    def __init__(self, name):
        self.name = name
        self.HWSetDB=mydb['hardware_sets']
        self.capacity = self.HWSetDB.find_one({"hw_set_name":self.name})['total_capacity']
        self.availability = self.HWSetDB.find_one({"hw_set_name":self.name})['available_capacity']
        
    def __set_capacity__(self):
        desired_cap = input("What should the capacity of this HWSet be? ")
        self.capacity = desired_cap
        self.availability = self.capacity
    
    # technical debt
    def add_HWSet_to_DB(self):
        pass

    def get_availability(self):
        self.availability = self.HWSetDB.find_one({"hw_set_name":self.name})['available_capacity']
        return self.availability

    def get_capacity(self):
        self.capacity = self.HWSetDB.find_one({"hw_set_name":self.name})['total_capacity']
        return self.capacity

    def get_checkedout_quantity(self):
        self.availability = self.HWSetDB.find_one({"hw_set_name":self.name})['available_capacity']
        self.capacity = self.HWSetDB.find_one({"hw_set_name":self.name})['total_capacity']
        return self.capacity - self.availability

    # in the case of a user checking out a qty of more units than available, an error code of -1 is returned
    # in addition, the availability is set to zero rather than the negative number stored in new_availability
    def check_out(self, qty):
        err_code = "Checkout"
        self.availability = self.get_availability()
        self.capacity = self.get_capacity()

        new_availability = self.availability - qty
        # if user attempts to check out more than available, they will check out the available amount, not requested amount
        if new_availability < 0:
            amt_checked_out = self.availability
            self.availability = 0
            err_code = "Tried to checkout more than available resources"

            #self.HWSetDB.update_one({"hw_set_name":self.name}, {"$set": {"available_capacity":int(self.availability), 
            #    "capacity_in_use":int(self.capacity)}})

            return err_code
        else:
            self.availability = new_availability
            self.HWSetDB.update_one({"hw_set_name":self.name}, {"$set": {"available_capacity":int(self.availability), 
                "capacity_in_use":(self.capacity - self.availability)}})
            return err_code


    # if user attempts to check in more than the HWSet capacity, the availability will be set to the capacity amount
    def check_in(self, qty):
        err_code = "Checked In"
        new_availability = self.availability + qty

    # if user attempts to check in more than the HWSet capacity, the availability will be set to the capacity amount
        if new_availability > self.capacity:
            err_code = ""
            amt_checked_in = self.capacity - self.availability
            self.availability = self.capacity

            #self.HWSetDB.update_one({"hw_set_name":self.name}, {"$set": {"available_capacity":int(self.availability), "capacity_in_use":0}})
            return err_code
        else:
            self.availability = new_availability
            #self.mycol.update_one({"project_id":self.project_id}, {"$set": {"hwSets."+str(self.name):self.hwSets[self.name]}})
            self.HWSetDB.update_one({"hw_set_name":self.name}, {"$set": {"available_capacity":int(self.availability), "capacity_in_use":(self.capacity-self.availability)}})
            return err_code

    