import os

basedir = os.path.abspath(os.path.dirname(__name__))
# (function call to the .env file for values)
class Config:
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')

