#!/usr/bin/python3
'''file that defines all common attributes for other classes'''
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        '''
        create new base model instance
        '''
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
            return
        for key, value in kwargs.items():
            if key in ['created_at', 'updated_at']:
                self.__dict__[key] = datetime.fromisformat(value)
            elif key != '__class__':
                self.__dict__[key] = value

    def __str__(self):
        '''defines string representation of object'''
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        '''updates the attritute when called'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''creates custom dictionary from __dict__'''
        my_dict = self__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
