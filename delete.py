import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


x = mycol.delete_one({'name': 'Amy'})

#x = mycol.delete_many({})

print(x.deleted_count, " documents deleted.")
