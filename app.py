from pymongo import MongoClient
from flask import Flask
from flask import jsonify
from flask import request
from bson.objectid import ObjectId

app = Flask(__name__)
server = MongoClient(
    'mongodb+srv://admin:Bko36aUgkprnlEsq@supercluster-e6ymx.mongodb.net/test?retryWrites=true&w=majority'
)
db = server.test
collection = db.users


@app.route('/users')
def get_all():
    users = collection.find({})
    array = []

    for user in users:
        user['_id'] = str(user['_id'])
        array.append(user)

    return jsonify(array)


@app.route('/users/<user_id>')
def get(user_id):
    user = collection.find_one({"_id": ObjectId(user_id)})
    user['_id'] = str(user['_id'])

    return jsonify(user)


@app.route('/users', methods=["POST"])
def create():
    collection.insert_one(request.form.to_dict())

    return jsonify(request.form)


@app.route('/users', methods=["DELETE"])
def delete_all():
    collection.remove({})

    return 'Success!'


@app.route('/users/<user_id>', methods=["DELETE"])
def delete(user_id):
    collection.remove(
        {
            '_id': ObjectId(user_id)
        }
    )

    return f'Delete {user_id}!'


@app.route('/users/<user_id>', methods=["PUT"])
def update(user_id):
    user = request.form.to_dict()

    collection.replace_one(
        {
            '_id': ObjectId(user_id)
        },
        user
    )

    return f'Update {user_id}!'


if __name__ == '__main__':
    app.run()
