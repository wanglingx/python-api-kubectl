import os
class Config(object):
    #Config File System Path
    basedir = os.path.abspath(os.path.dirname(__file__))
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')
    SECRET_KEY = os.getenv('SECRET_KEY', None)

    # MongoDB Config
    MONGODB_SETTINGS = {
        'db': os.getenv('MONGO_DB', 'project-cloud'),
        'host': os.getenv('MONGO_URI', 'xxxxxxxxxxxxxxxx')
    }
    
#config Environment
class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

class DebugConfig(Config):
    DEBUG = True

# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
