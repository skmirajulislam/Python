import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

# @activate it - /Applications/Python\ 3.12/Install Certificates.command

'''
SSL & TLS verification: -
@install certifi - pip install certifi
@activate it - /Applications/Python 3.12/Install Certificates.command
'''


class Connection:
    def __init__(self, password: str) -> None:
        self.password = password
        self.client = self.connect_mongodb_server()

    # ----- Connector Function -------- : -
    def connect_mongodb_server(self):
        uri = f"mongodb+srv://miraj:{self.password}@cluster0.tkzvadc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!\n")
            return client
        except Exception as err:
            print(err)
            return err

    # ----- Component Function -------- : -
    def connection_database(self):
        test_db = self.client.Users
        # or db-Folder name where Json will be stored.
        # If the name is not found, then same named new cluster is created.
        return test_db
        # Returning Client database Object

    def getDb_details(self):
        dbs = self.client.list_database_names()
        return dbs

    def getCollections(self):
        db = self.connection_database()  
        collection = db.list_collection_names()
        print(collection)


class Operations(Connection):

    def __init__(self, PassWord: str) -> None:
        super().__init__(PassWord)
        self.db = self.connection_database()

    # ------- Crud Function ------- : -
    def insert_document_to_db(self):
        collection = self.db.Users

        # PSON similar to JSON
        test_document = {
            'name': 'Miraj',
            'Email': 'skmirajulislam181@gmail.com',
            'PassWord': 'Cold786'
        }

        inserted_id = collection.insert_one(test_document).inserted_id
        print(f'{inserted_id} Data Sent to MongoDB Atlas..!')

    # ------- New database Creation ------- : -
    def create_new_database(self, nameDb: str):
        database_name = nameDb

        if database_name:
            new_db = self.client[database_name]
            print(f"Database '{database_name}' created successfully!")
        else:
            print("Please provide a valid name for the new database.")
            return None

        return new_db

    def send_document_to_new_database(self):

        collection = self.create_new_database('Person')

        if collection is not None:
            first_names = ['sk', 'Arnab', 'Shuvam', 'sk']
            last_names = ['Miraj', 'Das', 'Mondal', 'Sahil']
            ages = [18, 21, 22, 20]

            docs = []
            for first_name, last_name, age in zip(first_names, last_names, ages):
                doc = {'First_name': first_name,
                       'Last_name': last_name, 'Age': age}
                docs.append(doc)

                # collection.person_collection.insert_one(doc)
                # print("Document sent to the new database.")
            collection.person_collection.insert_many(docs)
            print("Document sent to the new database.")


class Query(Operations):

    def __init__(self, PassWord: str) -> None:
        super().__init__(PassWord)

    # ------- Retriving Data From DB ------- : -
    def find_all_persons(self):
        collections = self.create_new_database('Person')
        people = collections.person_collection.find()

        # print(list(people)) list of data

        for person in people:
            print(person)

    def find_someone_from_person(self):

        collections = self.create_new_database('Person')
        data = collections.person_collection.find_one({'First_name': 'sk'})
        print(data)

    def count_all_pepole(self):
        collections = self.create_new_database('Person')
        count = collections.person_collection.count_documents(filter={})
        print(count)

    def get_person_by_id(self, person_id):
        from bson.objectid import ObjectId

        _id = ObjectId(person_id)
        collections = self.create_new_database('Person')
        person = collections.person_collection.find_one({'_id': _id})
        print(person)

    def get_user_by_age_range(self, minAge, maxAge):
        # Query using MongoDB operators {age > minAge and age < maxAge}
        # query = {
        #     'Age': {'$gte': minAge, '$lte': maxAge}
        # }

        query = {'$and': [
                {'Age': {'$gte': minAge}},
                {'Age': {'$lte': maxAge}}
        ]}

        collections = self.create_new_database('Person')
        pepole = collections.person_collection.find(query).sort('Age')
        for Person in pepole:
            print(Person)

    def project_columns(self):
        columns = {'_id': 0, 'First_name': 1, 'Last_name': 1}
        collections = self.create_new_database('Person')
        pepole = collections.person_collection.find({}, columns)
        for Person in pepole:
            print(Person)

    def update_person_by_id(self, person_id):
        from bson.objectid import ObjectId

        _id = ObjectId(person_id)

        query = {
            # if field is exist, it will simply update it
            '$set': {'new_Fuild': True},
            '$inc': {'Age': 1},
            '$rename': {'First_name': 'Fast', 'Last_name': 'Last'}
        }

        collections = self.create_new_database('Person')
        collections.person_collection.update_one({'_id': _id}, query)
        # collections.person_collection.update_one({'_id': _id}, {'$unset':{'new_Fuild':' '}}) #unsetting value

    def replace_one(self, person_id):
        from bson.objectid import ObjectId

        _id = ObjectId(person_id)

        document = {
            'Fast_name': 'Sk Mirajul',
            'Last_name': 'Islam',
            'Age': 18
        }

        collections = self.create_new_database('Person')
        collections.person_collection.replace_one({'_id': _id}, document)

    def delete_doc_by_id(self, person_id):
        from bson.objectid import ObjectId
        _id = ObjectId(person_id)

        collections = self.create_new_database('Person')
        collections.person_collection.delete_one({'_id': _id})

    # ---------- Relation Ship Between JSON --------------------

    def add_address_embad(self, person_id, address):
        from bson.objectid import ObjectId
        _id = ObjectId(person_id)

        collections = self.create_new_database('Person')
        collections.person_collection.update_one(
            {'_id': _id}, {'$addToSet': {'addresses': address}})

    def add_address_relationship(self, person_id, address):
        from bson.objectid import ObjectId
        _id = ObjectId(person_id)

        address = address.copy()
        address['Ownerid'] = person_id
        collections = self.create_new_database('Person')
        addressCollections = collections.addresses
        addressCollections.insert_one(address)


def main() -> None:

    password = os.environ.get('MONGO_PASS')
    mongodb = Query(password)

    # db_List = mongodb.getDb_details()
    # print(db_List)

    # mongodb.getCollections()
    # mongodb.send_document_to_new_database()
    # mongodb.insert_document_to_db()
    mongodb.find_all_persons()
    # mongodb.find_someone_from_person()
    # mongodb.count_all_pepole()

    # mongodb.get_user_by_age_range(18, 20)
    # mongodb.project_columns()
    # mongodb.update_person_by_id('65fc6724a54b02c68347d045')
    # mongodb.replace_one('65fc6724a54b02c68347d045')
    # mongodb.get_person_by_id('65fc6724a54b02c68347d045')
    # mongodb.delete_doc_by_id('65fc6724a54b02c68347d048')

    address = {
        "_id": "62475964011a9126a4cebeb7",
        "street": "Bay Street",
        "number": 2706,
        "city": "San Francisco",
        "country": "United States",
        "zip": "94107"
    }

    # mongodb.add_address_embad('65fc6724a54b02c68347d045', address)
    # mongodb.add_address_relationship('65fd9886f6160de8de0804e5', address)


if __name__ == '__main__':
    main()
