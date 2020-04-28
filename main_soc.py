from flask_script import Manager, Shell
from peppa_soc import create_app, api
from peppa_soc import Env
from app import *
import logging

if Env == 'dev':
    app = create_app('dev')

elif Env == 'prod':
    app = create_app('prod')

elif Env == 'demo':
    app = create_app('demo')

manager = Manager(app)
manager.add_command("shell", Shell)

handler = logging.FileHandler('log/soc_log.log', encoding='UTF-8')
handler.setLevel(logging.DEBUG)
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(module)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)
app.logger.addHandler(handler)

api.namespaces = []
api.add_namespace(user_n)
api.add_namespace(waf_n)
api.add_namespace(scanner_n)
api.add_namespace(nids_n)
api.add_namespace(log_analysis_n)
api.add_namespace(honeypot_n)
api.add_namespace(hids_n)
api.add_namespace(bug_life_n)
api.add_namespace(assets_inventory_n)

if __name__ == '__main__':
    manager.run()

