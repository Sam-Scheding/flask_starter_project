from functools import wraps
from flask import request, jsonify
import bcrypt
from be.api.user.models import Salt, User


class AuthorisationService:

    def hashed_passwords_are_equal(password_attempt, hashed_password):
        return bcrypt.checkpw(password_attempt.encode('utf-8'), hashed_password)

    def generate_salt():
        return bcrypt.gensalt()


    def hash_password(password, salt):
        return bcrypt.hashpw(password.encode('utf-8'), salt)


    def is_authorized(user, password_attempt):

        if not user or not password_attempt:
            return False

        is_authorized = AuthorisationService.hashed_passwords_are_equal(
            password_attempt,
            user.hashed_password,
        )
        print(is_authorized)        
        return is_authorized


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = request.headers.get('x-access-token', None)

        if token is None:
            return jsonify({'message': 'No Access Token'})
