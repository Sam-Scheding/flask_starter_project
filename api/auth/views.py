import datetime
import jwt
from flask import Blueprint, jsonify, request
from be.services.authorisation_service import AuthorisationService
from be.services.user_service import UserService
from be.services.validation_service import ValidationService
from be.api.user.models import UserSchema
from be import config

blueprint = Blueprint('auth', __name__)


@blueprint.route('/login', methods=['POST'])
def login():

    body = request.get_json(force=True)
    email = body.get('email', None)
    password_attempt = body.get('password', None)

    if not ValidationService.is_valid_email(email) or not password_attempt:
        return jsonify({'message': 'Bad Request'}), 400

    user, message = UserService.get_user(email=email)
    is_authorized = AuthorisationService.is_authorized(user, password_attempt)

    if not is_authorized:
        return jsonify({'message': 'Unauthorised'}), 401

    token = jwt.encode({ 
        'public_id': user.public_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
    }, config.SECRET_KEY)  # TODO: Is this the correct way to access config inside the app?

    return jsonify({
        'token': token.decode('utf-8')
    }), 200


@blueprint.route('/register', methods=['POST'])
def register():

    body = request.get_json(force=True)
    email = body.get('email', None)
    password = body.get('password', None)

    user, message = UserService.create_user(email, password)

    if not user:
        return jsonify({'message': message}), 400

    serialised_user = UserSchema().dump(user)

    return jsonify(serialised_user), 200
