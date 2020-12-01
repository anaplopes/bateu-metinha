# -*- coding: utf-8 -*-
import json
from datetime import datetime
from core.app import started_date
from flask.views import MethodView
from flask import Blueprint, jsonify


bp_status = Blueprint('status', __name__, url_prefix='/')
class Live(MethodView):
    
    def get(self):
        """ Rota de status da api """
        
        with open('package.json', 'r') as pk:
            file = json.load(pk)

            payload = {
                'name': file['name'],
                'version': file['version'],
                'started': started_date,
                'uptime': str(datetime.now() - started_date)
            }
            return jsonify(payload), 200


bp_status.add_url_rule('/', view_func=Live.as_view('status'), methods=['GET'])