# app/__init__.py

from flask_api import FlaskAPI

# local import
from instance.config import app_config
from flask import request, jsonify, abort

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    @app.route('/words', methods=['GET'])
    def words():
        if request.method == "GET":
            response = jsonify({
                'wysiwyg': 'Hello, world!'
            })
            response.status_code = 200
            return response

    return app