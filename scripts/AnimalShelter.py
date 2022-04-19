from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, credentials):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        self.username = credentials['username']
        self.password = credentials['password']
        self.client = MongoClient('mongodb://%s:%s@localhost:27017/AAC?authSource=admin' % (self.username, self.password))
     
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            is_valid_insertion = self.database.animals.insert(data) # data should be dictionary    
            if is_valid_insertion:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            result = list(self.database.animals.find(data, {"_id": False}))
            return result
        else:
            raise Exception("Nothing to save, because data parameter is empty")
