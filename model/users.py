from database.database import collection
from bson.objectid import ObjectId


class UsersModel:
    collection = collection

    def get(self, user_id):
        user = self.collection.find_one({
            "_id": ObjectId(user_id)
        })
        user['_id'] = str(user['_id'])

        return user

    def get_all(self):
        users = self.collection.find({})

        return list(users)

    def create(self, data):
        result = self.collection.insert_one(data.to_dict())

        return self.get(result.inserted_id)

    def delete(self, user_id):
        result = self.get(user_id)

        self.collection.remove({
            '_id': ObjectId(user_id)
            }
        )

        return result

    def delete_all(self):
        self.collection.remove({})

    def update(self, data, user_id):
        self.collection.replace_one({
            '_id': ObjectId(user_id)
        },
            data
        )

        return self.get(user_id)
