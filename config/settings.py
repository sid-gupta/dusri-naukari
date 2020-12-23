import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__package__))


class DevelopmentConfig:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 289
    }

    REMEMBER_COOKIE_DURATION = timedelta(days=90)

    WTF_CSRF_TIME_LIMIT = None


class ProductionConfig(DevelopmentConfig):
    SECRET_KEY = 'production ready secret here'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
