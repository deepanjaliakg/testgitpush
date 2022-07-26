import pymongo
client = pymongo.MongoClient("mongodb+srv://deepanjali:*muthappa@cluster0.cj5ggfq.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name":"deepa",
     "emailid":"deepanjali@gmail.com"}
db1 = client['mongotest']
coll = db1['test']
coll. insert_one(d)