from .default import *
# Parámetros para activar el modo debug
class Configuracion(DefaultConfig):
    # Parámetros para activar el modo debug
    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    APP_ENV = APP_ENV_TESTING
    SQLALCHEMY_DATABASE_URI = 'mysql://root:S1st3m45@127.0.0.1/flask_test'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
    # SQLALCHEMY_BINDS = {
    #     'database': 'mysql://root:S1st3m45@localhost/flask_tuto'
    # }
    