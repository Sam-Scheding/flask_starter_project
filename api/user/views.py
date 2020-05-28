from flask import Blueprint, jsonify, request
from be.services.user_service import UserService 
from .models import UserSchema

blueprint = Blueprint('user', __name__)
    

@blueprint.route('/user/<string:public_id>', methods=['GET']) # TODO: Use session cookie to get user instead
def read_user(public_id):

    user, message = UserService.get_user(public_id=public_id)

    if not user:
        return jsonify({'message': message}), 404

    serialised_user = UserSchema().dump(user)

    return jsonify(serialised_user), 200


@blueprint.route('/user/<string:public_id>', methods=['PATCH'])
def update_user(public_id):
    
    body = request.get_json(force=True)
    user, message = UserService.update_user(public_id=public_id, fields=body)

    if not user:
        return jsonify({'message': message}), 404

    serialised_user = UserSchema().dump(user)

    return jsonify(serialised_user), 200


@blueprint.route('/user/<string:public_id>', methods=['DELETE'])
def delete_user(public_id):

    success, message = UserService.delete_user(public_id=public_id)

    if not success:
        return jsonify({'message': message}), 404

    return jsonify({'message': message}), 200
