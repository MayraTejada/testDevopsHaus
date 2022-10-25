import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    #Database URL
    SQLALCHEMY_DATABASE_URI =  'mysql://admin:Redeban2022*@database-1.cvfo0tjysyng.us-east-1.rds.amazonaws.com:3306/mydatabasehaus'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
