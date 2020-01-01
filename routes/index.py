from controllers.users import UsersController


def routes(app, request, jsonify, abort):
    user_controller = UsersController(jsonify, abort)

    @app.route('/users/<user_id>', methods=["GET"])
    def get(user_id):
        return user_controller.get(user_id)

    @app.route('/users', methods=["GET"])
    def get_all():
        return user_controller.get_all()

    @app.route('/users', methods=["POST"])
    def create():
        return user_controller.create(request.form)

    @app.route('/users/<user_id>', methods=["DELETE"])
    def delete(user_id):
        return user_controller.delete(user_id)

    @app.route('/users', methods=["DELETE"])
    def delete_all():
        return user_controller.delete_all()

    @app.route('/users/<user_id>', methods=["PUT"])
    def update(user_id):
        return user_controller.update(request.form, user_id)
