# -*- coding: utf-8 -*-
from datetime import datetime
from core.services.db_execution import DbExecutionService


class WorkerLogRepository:
    
    def __init__(self):
        self.db = DbExecutionService(collection='log')


    def list(self, args=None):
        if 'date' in args:
            dt = datetime.strptime(args['date'], "%Y-%m-%d")
            args.update({'date': {'$lt': datetime.utcnow(), '$gte': dt}})
        
        logs = self.db.find(params=args, sort='date')
        return {
            'statusCode': 200,
            'output': {
                'data': logs,
                'qtd_registro': len(logs),
                'error': None,
                'isValid': True
            }
        }


    def read(self, args=None):
        log = self.db.find_one(params=args)
        if not log:
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
                'data': log,
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
                'message': 'Log saved successfully',
                'error': None,
                'isValid': True
            }
        }
