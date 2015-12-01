from pymongo import MongoClient


client = MongoClient()
client = MongoClient('localhost', 27017)

db = client.test_database
collection = db.test_collection

result = db.posts.delete_many({})
print(result.deleted_count)


post = {"author": "Mike","text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"]}
posts = db.posts
post_id = posts.insert_one(post).inserted_id

post = {"author": "lollo","text": "My blog post!", "tags": ["uppo", "python", "poppo"]}
posts = db.posts
post_id = posts.insert_one(post).inserted_id


def re(self):
   return posts.find_one({"author": "Mike"})


def nn(self):
    for post in posts.find():
        print(post)

    return posts.find()


