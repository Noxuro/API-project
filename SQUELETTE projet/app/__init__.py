# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 11:01:29 2021

@author: etudiant
"""

from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
app = Flask(__name__)

SWAGGER_URL='/swagger' 
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT= get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name' : "Todo List API"
    }
)
app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

from app import views