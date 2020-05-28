import datetime
import uuid
from be.services.database_service import db
from be.services.serialiser_service import ma

class User(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    email = db.Column(db.String(128), unique=False, nullable=False)
    hashed_password = db.Column(db.String(128), unique=False, nullable=False)
    is_activated = db.Column(db.Boolean, unique=False, nullable=False)
    is_deleted = db.Column(db.Boolean, unique=False, nullable=False)
    is_admin = db.Column(db.Boolean, unique=False, nullable=False)
    public_id = db.Column(db.String(36), unique=True, nullable=False)

    def __init__(self, email, hashed_password):
        self.created_at = datetime.datetime.utcnow()
        self.email = email
        self.is_activated = True  # TODO: Send activation email on register
        self.is_admin = False
        self.is_deleted = False
        self.hashed_password = hashed_password
        self.public_id = str(uuid.uuid4())

class UserSchema(ma.Schema):
    class Meta:
        fields = (
            'created_at',
            'email', 
            'is_activated', 
            'is_admin', 
            'public_id',
        )

# TODO: Delete this record when the corresponding user is deleted
class Salt(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    email = db.Column(db.String, db.ForeignKey(User.email))
    salt = db.Column(db.String, unique=False, nullable=False)

    def __init__(self, email, salt):
        
        self.email = email
        self.salt = salt
