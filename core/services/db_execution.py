# -*- coding: utf-8 -*-
from datetime import datetime
from bson.objectid import ObjectId
from core.services.db_connection import DbConnectionService


class DbExecutionService:
    """ Serviço responsável por executar comandos no db. """
    
    def __init__(self, collection):
        self.db = DbConnectionService()
        self.collection = collection
    
    
    def __convert_to_string(self, row):
        for i in row:
            if isinstance(row[i], ObjectId):
                row[i] = str(row[i])
                
            if isinstance(row[i], datetime):
                row[i] = row[i].strftime("%Y-%m-%dT%H:%M:%S.%f%z")
                
        return row
    

    def find_one(self, params={}):
        if not isinstance(params, dict):
            raise TypeError('param must be a object')
        
        if '_id' in params:
            params.update({'_id': ObjectId(params['_id'])})
        
        session = self.db.create_connection(self.collection)
        result = session.find_one(params)
        if not result:
            return result
        return self.__convert_to_string(result)
    

    def find(self, params={}, select_coll=None, sort=None, order=1, limit=None):
        if not isinstance(params, dict):
            raise TypeError('param must be a object')

        if '_id' in params:
            params.update({'_id': ObjectId(params['_id'])})
        
        session = self.db.create_connection(self.collection)
        if sort:
            if limit:
                return list(map(self.__convert_to_string, session.find(params, select_coll).sort(sort, order).limit(limit)))
            return list(map(self.__convert_to_string, session.find(params, select_coll).sort(sort, order)))
        # return list(map(lambda row: {i: str(row[i]) if isinstance(row[i], ObjectId) else row[i] for i in row}, session.find(param)))
        return list(map(self.__convert_to_string, session.find(params, select_coll))) 
    
    
    def insert_one(self, data_obj):
        if not isinstance(data_obj, dict):
            raise TypeError('data must be a object.')
            
        session = self.db.create_connection(self.collection)
        return session.insert_one(data_obj)


    def insert_many(self, data_list):
        if not isinstance(data_list, list):
            raise TypeError('data must be a list of object.')
        
        for data in data_list:
            if not isinstance(data_list[data], dict):
                raise TypeError(f'data <{data}> must be a object.')
        
        session = self.db.create_connection(self.collection)
        return session.insert_many(data_list)
    

    def upsert(self, query_obj, data_obj):
        if not isinstance(query_obj, dict):
            raise TypeError('query must be a object')

        if not isinstance(data_obj, dict):
            raise TypeError('data must be a object')
        
        if '_id' in query_obj:
            query_obj.update({'_id': ObjectId(query_obj['_id'])})
        
        if '_id' in data_obj:
            data_obj.update({'_id': ObjectId(data_obj['_id'])})

        session = self.db.create_connection(self.collection)
        return session.update(query_obj, { "$inc": data_obj }, upsert=True)
    
    
    def update_one(self, id, data_obj):
        if not isinstance(data_obj, dict):
            raise TypeError('data must be a object')

        session = self.db.create_connection(self.collection)
        return session.update_one({'_id': ObjectId(id)}, { "$set": data_obj })


    def update_many(self, query_obj, data_obj):
        if not isinstance(query_obj, dict):
            raise TypeError('query must be a object')

        if not isinstance(data_obj, dict):
            raise TypeError('data must be a object')
        
        if '_id' in query_obj:
            query_obj.update({'_id': ObjectId(query_obj['_id'])})
        
        if '_id' in data_obj:
            data_obj.update({'_id': ObjectId(data_obj['_id'])})
        
        session = self.db.create_connection(self.collection)
        return session.update_many(query_obj, { "$set": data_obj })
    
    
    def delete(self, id):
        session = self.db.create_connection(self.collection)
        return session.delete_one({'_id': ObjectId(id)})
