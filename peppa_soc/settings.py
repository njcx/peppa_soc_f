import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    Redis_Host = '127.0.0.1'
    Redis_Port = 6379
    Redis_Pw = ''

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class DemoConfig(Config):
    DEBUG = True


class ProductionConfig(Config):

    Redis_Host = ''
    Redis_Port = 6379
    Redis_Pw = ''

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'prod': ProductionConfig,
    'dev': DevelopmentConfig,
    'demo': DemoConfig,
}


Env = 'prod'
