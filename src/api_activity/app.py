from flask import Flask, jsonify
from flask_restful import Resource ,Api, reqparse


class Hello(Resource):
    def get(self):
        return jsonify({"message": "Hello, World!"})
    
class Echo(Resource):
# Use RequestParser to parse the arguments from the request.
# Don't reinvent the wheel! We could write a parser ourselves,
# but let's use one that was already made for us!
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('arg1', type=str, location='args')
        parser.add_argument('arg2', type=str, location='args')
        arguments = parser.parse_args()
        return jsonify(arguments)
    
class Square(Resource):
    def get(self, num):
        return jsonify({'Shape': __class__.__name__, 'Value': num ** 2})

def init_api(app: Flask) -> None:
    api = Api(app)

    api.add_resource(Hello, '/')
    api.add_resource(Echo, '/echo')
    api.add_resource(Square, '/square/<int:num>')

def create_app() -> Flask:
    app = Flask(__name__)
    init_api(app)
    return app
    
def run_app(debug: bool = True) -> None:
    create_app().run(debug=debug)
    
if __name__ == "__main__":
    run_app()