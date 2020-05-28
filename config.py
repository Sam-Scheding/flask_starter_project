import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

FLASK_DEBUG = True # TODO: Doesn't work

FLASK_ENV = 'development' # TODO: Doesn't work

SECRET_KEY = 'secret'

# Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite'))
SQLALCHEMY_TRACK_MODIFICATIONS =  False
