import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or  '07479fa1-a858-4f66-bb0c-5f8cfc0a1ae6'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def init_app(app):
        pass

class DevelopmentConfig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(base_dir, 'sitio.db')

class TestingConfig(Config):
    debug = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(base_dir, 'sitio.db')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(base_dir, 'sitio.db')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = { 
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


