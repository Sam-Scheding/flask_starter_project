import os
from flask import Flask
from be.services.database_service import db
from be.services.serialiser_service import ma
from be.api.user.views import blueprint as user_blueprint
from be.api.auth.views import blueprint as auth_blueprint

def create_app():

    # Create application instance
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    db.init_app(app)

    ma.init_app(app)

    #Register Blueprints
    app.register_blueprint(user_blueprint, url_prefix='/api/v1/')
    app.register_blueprint(auth_blueprint, url_prefix='/api/v1/')


    # Print routes
    print('Registered routes: ')
    for rule in app.url_map.iter_rules():
        print('\t- {} {}'.format(rule.rule, rule.methods))

    if not os.path.isfile(os.path.join(app.config['BASE_DIR'], 'db.sqlite')):
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
