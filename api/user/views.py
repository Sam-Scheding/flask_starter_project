
from flask import Blueprint, jsonify, request
from be.services.user_service import UserService 
blueprint = Blueprint('user', __name__)


@blueprint.route('/user/', methods=['POST'])
def create_user():

    body = request.get_json(force=True)
    email = body.get('email', None)
    password = body.get('password', None)

    user, message = UserService.create_user(email, password)

    if not user:
        return jsonify({'message': message}), 400

    return jsonify(user), 200
    

@blueprint.route('/user/<string:email>', methods=['GET']) # TODO: Use session cookie to get user instead
def read_user(email):

    user, message = UserService.get_user(email=email)

    if not user:
        return jsonify({'message': message}), 404

    return jsonify(user), 200


@blueprint.route('/user/<string:email>', methods=['PATCH'])
def update_user(email):
    
    body = request.get_json(force=True)
    user, message = UserService.update_user(email=email, fields=body)

    if not user:
        return jsonify({'message': message}), 404

    return jsonify(user), 200 


@blueprint.route('/user/<string:email>', methods=['DELETE'])
def delete_user(email):

    success, message = UserService.delete_user(email=email)
    
    if not success:
        status = 404

    return jsonify({'message': message}), 200
