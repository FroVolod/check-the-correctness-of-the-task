from pathlib import Path


class Configuration(object):
    DEBUG = True
    TESTS_FOLDER = Path('./test_db').resolve()
    USERS = {
        "admin": "admin",
        "qwe": "qweqwe",
    }
    BASE_URL = 'http://127.0.0.1:5000/'
