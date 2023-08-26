from flask import Flask
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix
from .controllers import todo_namespace

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config['RESTX_ERROR_404_HELP'] = False
api = Api(
    app,
    version='1.0',
    title='TodoMVC API',
    description='A simple TodoMVC API',
)

api.add_namespace(todo_namespace)
