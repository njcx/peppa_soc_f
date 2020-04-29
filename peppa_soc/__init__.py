from .settings import *
from flask import Flask
from flask_restx import Api
from flask_login import LoginManager
login_manager = LoginManager()

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Waf-API-Token'
    }
}

api = Api(version="V1.0",
          title="WAF API",
          description="This waf api powered by Flask",
          authorizations=authorizations,
          security='apikey')

if Env == 'prod':
    api = Api(version="V1.0",
              title="WAF API",
              description="This waf api powered by Flask",
              authorizations=authorizations,
              security='apikey',
              doc=False)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    api.init_app(app)
    login_manager.init_app(app)
    return app
