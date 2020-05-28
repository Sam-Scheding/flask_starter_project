import bcrypt
from be.api.user.models import User, Salt
from .database_service import db
from .validation_service import ValidationService
from .authorisation_service import AuthorisationService

class UserService:

    def create_user(email, password):
        
        if not ValidationService.is_valid_email(email):
            return None, 'Invalid email'
        
        if not ValidationService.is_valid_password(password):
            return None, 'Invalid password'

        # TEST: User can delete and then recreate an account with the same email
        user = User.query.filter_by(email=email, is_deleted=False).first()
        if user:
            return None, 'User exists'

        salt = AuthorisationService.generate_salt()
        hashed_password = AuthorisationService.hash_password(password, salt)

        new_salt = Salt(email, salt)
        new_user = User(email, hashed_password)

        db.session.add(new_salt)
        db.session.add(new_user)
        db.session.commit()

        return new_user, 'Success'


    def get_user(*args, **kwargs):

        # TEST: User can't get a deleted user
        user = User.query.filter_by(**kwargs, is_deleted=False).first()

        if not user: # TEST: User can't get a non-existent user
            return None, 'No such user' 

        return user, 'Success'

    def update_user(email=None, fields={}):
        
        if not ValidationService.is_valid_email(email):
            return None, 'Invalid email'

        # TEST: User can't update a deleted user
        user = User.query.filter_by(email=email, is_deleted=False).first()

        if not user:
            return None, 'No such user'

        # TEST: Can't promote user to admin
        user.email = fields.get('email', user.email)
        user.is_activated = fields.get('is_activated', user.is_activated)

        return user, 'Success'

    def delete_user(email=None):

        if not ValidationService.is_valid_email(email):
            return False, 'Invalid email'

        # TEST: User can't update a deleted user
        user = User.query.filter_by(email=email, is_deleted=False).first()

        if not user:
            return False, 'No such user'

        user.is_deleted = True
        db.session.commit()

        return True, 'Success'
