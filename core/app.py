# -*- coding: utf-8 -*-
import os
from flask import Flask
from datetime import datetime
from flask_cors import CORS


started_date = datetime.now()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app_settings = os.getenv('APP_SETTINGS', 'config.DevelopmentConfig')
    app.config.from_object(app_settings)

    # models

    # controllers
    from core.controllers.status import bp_status
    app.register_blueprint(bp_status)
    
    from core.controllers.log import bp_log
    app.register_blueprint(bp_log)
    
    from core.controllers.pride import bp_pride
    app.register_blueprint(bp_pride)

    return app
