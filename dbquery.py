import pymongo
client = pymongo.MongoClient("mongodb+srv://pycharmers:McCombs2022@cluster-pycharmers.riszv1q.mongodb.net/?retryWrites=true&w=majority")
mydb=client['resource_management']

# Database connection to a user with only their name
# Used to login user
class creds_auth(object):
    def __init__(self,username):
        self.username=username
        self.mycol=mydb['users']

    # gets the password of the user the object represents
    def findPass(self):
        res=self.mycol.find_one({"username":self.username})
        return res['password']

# Child class of creds_auth that connects with the database - needs their password
# Used to Signup user
class creds_new(creds_auth):
    def __init__(self, username,password):
        super().__init__(username)
        self.password=password

    # Creates new user in database
    def create_user(self):
        user_document = {"username": self.username, "password": self.password}
        self.mycol.insert_one(user_document)

    # Checks if the user exists in the database
    # TODO: MAYBE Refactor - might be able to achieve same functionality in parent class because
    #           password is not needed
    def is_existing_user(self):
        user_found = self.mycol.find_one({"username":self.username})
        if (user_found):
            return True
        else:
            return False

# Database connection to an existing project
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
    
    # Gets the projects HW Usage for each HW Set
    def get_usage(self):
        project_details=self.mycol.find_one({"project_id":self.__project_id},{'_id':0})
        capacity_hwsets={}
        hwsets=self.hwsets.find()
        for i in hwsets:
            capacity_hwsets.update({i['hw_set_name']:i['total_capacity']})
        project_details.update({'capacity':capacity_hwsets})
        return project_details

# database connection to create a new project
# used for creating a new project 
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

# Class to connect to Hardware Sets
class HWSet:
    def __init__(self, name, id):
        self.name = name
        self.HWSetDB=mydb['hardware_sets']
        self.capacity = self.HWSetDB.find_one({"hw_set_name":self.name})['total_capacity']
        self.availability = self.HWSetDB.find_one({"hw_set_name":self.name})['available_capacity']
        
        self.projectDB=mydb['projects']
        self.project_id=int(id)
        self.selected_project=self.projectDB.find_one({'project_id':self.project_id})

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
        err_code = "Success"
        self.availability = self.get_availability()
        self.capacity = self.get_capacity()
        
        cur_qty=self.selected_project['hwSets'][self.name]
        quantity_=int(qty)
        updated_qty=cur_qty+quantity_
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

            
            self.projectDB.update_one({"project_id":self.project_id}, {"$set": {"hwSets."+str(self.name):updated_qty}})
            return err_code

    # if user attempts to check in more than the HWSet capacity, the availability will be set to the capacity amount
    def check_in(self, qty):
        err_code = "Success"
        new_availability = self.availability + qty

        cur_qty=int(self.selected_project['hwSets'][self.name])
        quantity_=int(qty)
        updated_qty=cur_qty-quantity_
    # if user attempts to check in more than the HWSet capacity, the availability will be set to the capacity amount
        if new_availability > self.capacity:
            err_code = "Tried to checkin more than available resources"
            amt_checked_in = self.capacity - self.availability
            self.availability = self.capacity
            return err_code
        else:
            self.availability = new_availability
            self.projectDB.update_one({"project_id":self.project_id}, {"$set": {"hwSets."+str(self.name):updated_qty}})
            self.HWSetDB.update_one({"hw_set_name":self.name}, {"$set": {"available_capacity":int(self.availability), "capacity_in_use":(self.capacity-self.availability)}})
            return err_code