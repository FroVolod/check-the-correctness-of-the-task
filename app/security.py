from flask import abort

from flask_httpauth import HTTPBasicAuth

from . import app


auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username in app.config['USERS']:
        return app.config['USERS'][username]
    return None

@auth.error_handler
def unauthorized():
    return abort(401)
    