# -*- coding: utf-8 -*-
import sys
import json
import traceback
from datetime import datetime
from flask.views import MethodView
from flask import Blueprint, jsonify, request
from core.repositories.worker_pride import WorkerPrideRepository


bp_pride = Blueprint('pride', __name__, url_prefix='/api/pride')
class Pride(MethodView):
    
    def get(self, id=None):
        query_string = dict(request.query_string) if request.query_string else None

        try:
            if id is None:
                response = self.worker.list(query_string)
            else:
                response = self.worker.read(payload={'_id': id})
            return jsonify({'output': response['output']}), response['statusCode']
            
        except Exception:
            return jsonify({
                'output': {
                    'data': [],
                    'error': traceback.format_exc(),
                    'isValid': False
                }
            }), 500


    def post(self):
        try:
            payload = request.get_json()
            response = self.worker.create(payload=payload)
            return jsonify({'output': response['output']}), response['statusCode']
            
        except Exception:
            return jsonify({
                'output': {
                    'data': [],
                    'error': traceback.format_exc(),
                    'isValid': False
                }
            }), 500

    
    def put(self, id):
        try:
            payload = request.get_json()
            response = self.worker.update(id=id, payload=payload)
            return jsonify({'output': response['output']}), response['statusCode']
            
        except Exception:
            return jsonify({
                'output': {
                    'data': [],
                    'error': traceback.format_exc(),
                    'isValid': False
                }
            }), 500


view = Pride.as_view('pride')
bp_log.add_url_rule('/', view_func=view, methods=['GET'])
bp_log.add_url_rule('/<id>', view_func=view, methods=['GET'])
bp_log.add_url_rule('/create', view_func=view, methods=['POST'])