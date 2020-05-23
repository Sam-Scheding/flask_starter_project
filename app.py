import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .services.database_service import db
from be.api.user.views import blueprint as user_blueprint

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite'))

def create_app():
    # Create application instance
    app = Flask(__name__)

    # Configure
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True
    app.config['FLASK_ENV'] = 'development'

    db.init_app(app)
    
    #Register Blueprints
    app.register_blueprint(user_blueprint, url_prefix='/api/v1/')

    # Print routes
    print('Registered routes: ')
    for rule in app.url_map.iter_rules():
        print('\t- {} {}'.format(rule.rule, rule.methods))

    if not os.path.isfile(os.path.join(BASE_DIR, 'db.sqlite')):
        setup_database(app)

    return app


def setup_database(app):

    print('Creating new DB')
    with app.app_context():
        db.create_all()

    # user = User()
    # user.username = "Tom"
    # db.session.add(user)
    # db.session.commit()


if __name__ == '__main__':
    app = create_app()
