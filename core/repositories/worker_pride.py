# -*- coding: utf-8 -*-
from datetime import datetime
from core.services.db_execution import DbExecutionService


class WorkerPrideRepository:
    
    def __init__(self):
        self.db = DbExecutionService(collection='pride')


    def list(self, payload=None):
        pride = self.db.find(params=payload)
        return {
            'statusCode': 200,
            'output': {
                'data': pride,
                'qtd_registro': len(pride),
                'error': None,
                'isValid': True
            }
        }


    def read(self, payload=None):
        pride = self.db.find_one(params=payload)
        if not pride:
            return {
                'statusCode': 404,
                'output': {
                    'data': [],
                    'error': 'Id does not exist',
                    'isValid': False
                }
            }
            
        return {
            'statusCode': 200,
            'output': {
                'data': pride,
                'error': None,
                'isValid': True
            }
        }


    def create(self, payload):
        if not payload:
            return {
                'statusCode': 400,
                'output': {
                    'data': [],
                    'error': 'I was expecting a payload, but apparently on is missing',
                    'isValid': False
                }
            }
        
        payload['date'] = datetime.utcnow()
        self.db.insert_one(data_obj=payload)
        return {
            'statusCode': 201,
            'output': {
                'data': [],
                'message': 'Pride saved successfully',
                'error': None,
                'isValid': True
            }
        }


    def update(self, id, payload):
        if not id or not payload:
            return {
                'statusCode': 400,
                'output': {
                    'data': [],
                    'error': 'I was expecting a id and a payload, but apparently on (or both) is missing',
                    'isValid': False
                }
            }
        
        pride = self.db.find_one(params={'_id': id})
        if not pride:
            return {
                'statusCode': 404,
                'output': {
                    'data': [],
                    'error': 'Id does not exist',
                    'isValid': False
                }
            }
        
        self.db.update_one(id=id, data_obj=payload)
        return {
            'statusCode': 200,
            'output': {
                'data': [],
                'message': 'Pride updated successfully',
                'error': None,
                'isValid': True
            }
        }
