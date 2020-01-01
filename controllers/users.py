from model.users import UsersModel


class UsersController:
    users_model = UsersModel()

    def __init__(self, jsonify, abort):
        self.jsonify = jsonify
        self.abort = abort

    def get(self, user_id):
        try:
            user = self.users_model.get(user_id)
            return self.jsonify(user)
        except:
            self.abort(500, 'Server error')

    def get_all(self):
        try:
            users = self.users_model.get_all()
            return self.jsonify(users)
        except:
            self.abort(500, 'Server error')

    def create(self, data):
        try:
            user = self.users_model.create(data)
            return self.jsonify(user)
        except:
            self.abort(500, 'Server error')

    def delete(self, user_id):
        try:
            user = self.users_model.delete(user_id)
            return self.jsonify(user)
        except:
            self.abort(500, 'Server error')

    def delete_all(self):
        try:
            self.users_model.delete_all()
            return self.jsonify({
                'message': 'success'
            })
        except:
            self.abort(500, 'Server error')

    def update(self, data, user_id):
        try:
            user = self.users_model.update(data, user_id)
            return self.jsonify(user)
        except:
            self.abort(500, 'Server error')
