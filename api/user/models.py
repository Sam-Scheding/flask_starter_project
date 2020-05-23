from be.services.database_service import db

class User(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    email = db.Column(db.String(128), unique=False, nullable=False)
    password_hash = db.Column(db.String(128), unique=False, nullable=False)
    activated = db.Column(db.Boolean, unique=False, nullable=False)
    deleted = db.Column(db.Boolean, unique=False, nullable=False)

    def __init__(self, email, password_hash):
        self.email = email
        self.password_hash = password_hash
        self.deleted = False
        self.activated = True  # TODO: Send activation email on register


class Salt(db.Model):
    email = db.Column(db.String, db.ForeignKey(User.email), primary_key=True)
    salt = db.Column(db.String, nullable=False)

    def __init__(self, email, salt):
        
        self.email = email
        self.salt = salt
