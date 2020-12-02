# -*- coding: utf-8 -*-
import sys
import json
import traceback
from flask.views import MethodView
from flask import Blueprint, jsonify, request
from core.repositories.worker_pride import WorkerPrideRepository


bp_pride = Blueprint('pride', __name__, url_prefix='/api')
class Pride(MethodView):
    
    def __init__(self):
        self.worker = WorkerPrideRepository()
    
    def get(self, id=None):
        args = dict(request.args) if request.args else {}

        try:
            if id is None:
                response = self.worker.list(args=args)
            else:
                response = self.worker.read(args={'_id': id})
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
bp_pride.add_url_rule('/pride/', view_func=view, methods=['GET', 'POST'])
bp_pride.add_url_rule('/pride/<id>/', view_func=view, methods=['GET', 'PUT'])
