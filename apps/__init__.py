from fastapi import FastAPI
from importlib import import_module
from mongoengine import connect

def router_include(app):
    for module_name in ('auth',):
        module = import_module('apps.service.{}.routes'.format(module_name))
        #app.include_router(module.router, prefix=f'/{module_name}', tags=[module_name.capitalize()])
        app.include_router(module.router)
        
def db_connect(config):
    # Extract MongoDB settings from the config object
    mongo_db = config.MONGODB_SETTINGS.get('db')
    mongo_host = config.MONGODB_SETTINGS.get('host')
    connect(db=mongo_db, host=mongo_host)

def create_app(config):
    app = FastAPI()
    app.config = config
    db_connect(config)
    router_include(app)
    return app
    
