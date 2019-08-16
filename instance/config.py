import os


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = 'postgres://taaiuzxnpynhvd:fca00cd20137a6cac1223b2fe199c24b87cbea54bb1bef07c93151f832f301fb@ec2-54-75-238-138.eu-west-1.compute.amazonaws.com:5432/ds7rvlbfqkfd2'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost/test_db'


class ProductionConfig(Config):
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'podtoin': ProductionConfig
}