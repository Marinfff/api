from flask import Flask
from flask import request
from flask import jsonify
from flask import abort
from routes.index import routes

app = Flask(__name__)
routes(app, request, jsonify, abort)

if __name__ == '__main__':
    app.run()
