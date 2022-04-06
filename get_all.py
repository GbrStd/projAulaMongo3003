import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydoc = mycol.find({}, {"_id": 0}).sort("name", 1)

for x in mydoc:
    print(x)
