import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'ahuiufkjjk'
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


User = [{'name': 'test', 'passwd': "098f6bcd4621d373cade4e832627b4f6"},
        {'name': 'njcx', 'passwd': "b23ab49fa9fbf142b809f2279ddec04b"}]