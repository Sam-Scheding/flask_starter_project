import bcrypt
from be.api.user.models import User, Salt
from .database_service import db
from .validation_service import ValidationService

class UserService:

    def create_user(email, password):
        
        if not ValidationService.is_valid_email(email):
            return None, 'Invalid email'
        
        if not ValidationService.is_valid_password(password):
            return None, 'Invalid password'

        # TEST: User can delete and then recreate an account with the same email
        user = User.query.filter_by(email=email, deleted=False).first()
        if user:
            return None, 'User exists'

        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)

        salt_model = Salt(email, salt)
        user_model = User(email, password_hash)

        db.session.add(salt_model)
        db.session.add(user_model)
        db.session.commit()

        return {
            'email': user_model.email,
            'activated': user_model.activated,
        }, 'Success'


    def get_user(email=None):

        if not ValidationService.is_valid_email(email):
            return None, 'Invalid email'

        # TEST: User can't get a deleted user
        user = User.query.filter_by(email=email, deleted=False).first()

        if not user: # TEST: User can't get a non-existent user
            return None, 'No such user' 

        return {
            'email': user.email,
            'activated': user.activated,
        }, 'Success'

    def update_user(email=None, fields={}):

        
        if not ValidationService.is_valid_email(email):
            return None, 'Invalid email'

        # TEST: User can't update a deleted user
        user = User.query.filter_by(email=email, deleted=False).first()

        if not user:
            return None, 'No such user'

        user.email = fields.get('email', user.email)
        user.activated = fields.get('activated', user.activated)

        return {
            'email': user.email,
            'activated': user.activated,
        }, 'Success'

    def delete_user(email=None):

        if not ValidationService.is_valid_email(email):
            return False, 'Invalid email'

        # TEST: User can't update a deleted user
        user = User.query.filter_by(email=email, deleted=False).first()

        if not user:
            return False, 'No such user'

        user.deleted = True
        db.session.commit()

        return True, 'Success'
