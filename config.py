# -*- coding: utf-8 -*-
import os.path
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, 'core/.env'))

class BaseConfig:
    """ Base configuration. """
    
    SECRET_KEY = os.getenv('SECRET_KEY', '')
    DEBUG = False
    # SESSION_COOKIE_NAME = os.getenv('SESSION_COOKIE_NAME', '')
    # STATIC_FOLDER = 'static'
    # TEMPLATES_FOLDER = 'templates'


class DevelopmentConfig(BaseConfig):
    """ Development configuration. """
    
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = os.getenv('DEV_DATABASE_URI', '')

    
class ProductionConfig(BaseConfig):
    """ Production configuration. """
    
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.getenv('PROD_DATABASE_URI', '')
