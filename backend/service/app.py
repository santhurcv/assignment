from flask import Flask
from .middleware import Middleware
from flask_restx import Api
from service.v1.user_views import api as ns1

ROOT_URL = '/myservice'
api = Api(
    title='My Service',
    version='1.0',
    description='service Details', doc='/swagger/document'
)


def create_app():

    app = Flask(__name__)

    app.config["APPLICATION_ROOT"] = ROOT_URL
    # db.init_app(app)

    api.add_namespace(ns1, path=ROOT_URL)
    api.init_app(app)

    app.wsgi_app = Middleware(app.wsgi_app)

    return app


