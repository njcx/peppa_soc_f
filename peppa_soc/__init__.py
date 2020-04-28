from sanic import Sanic
from sanic_restplus import Api
from sanic_restplus.restplus import restplus
from spf import SanicPluginsFramework
app = Sanic(__name__)
spf = SanicPluginsFramework(app)
rest_assoc = spf.register_plugin(restplus)


api = Api(version='1.0', title='TodoMVC API',
          description='A simple TodoMVC API')




