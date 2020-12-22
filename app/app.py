from flask import Flask
from config import config as application_configuration
from .extensions import db, migrate, login_manager, csrf
from .blueprints import main


def init_extensions(app):
    pass
    # db.init_app(app)
    # migrate.init_app(app, db)
    # login_manager.init_app(app)
    # csrf.init_app(app)


# def authentication():
#     login_manager.login_view = 'auth.login'
#
#     @login_manager.user_loader
#     def load_user(id):
#         try:
#             return User.query.get(id)
#         except Exception as e:
#             db.session.rollback()
#             return None


def create_app(config_name: str = 'default', override_settings=None):
    app = Flask(__name__)
    app.config.from_object(application_configuration[config_name])

    if override_settings:
        app.config.update(override_settings)

    init_extensions(app)
    # authentication()

    app.register_blueprint(main)

    return app