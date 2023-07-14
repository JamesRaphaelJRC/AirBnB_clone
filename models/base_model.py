#!/usr/bin/python3
''' Defines a class BaseModel '''
import uuid
from datetime import datetime
import models


class BaseModel:
    ''' Represents the BaseModel class '''
    def __init__(self, *args, **kwargs):
        ''' Initializes an instance of the BaseModel class'''
        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'name':
                    self.name = value
                elif key == 'my_number':
                    self.my_number = value
                elif key == 'id':
                    self.id = value
                elif key == 'created_at':
                    self.created_at = datetime.fromisoformat(value)
                elif key == 'updated_at':
                    self.updated_at = datetime.fromisoformat(value)
        else:
            self.name = None
            self.my_number = None
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            models.storage.new(self)

    def save(self):
        ''' Updates the public instance attribute 'updated_at' with the current
            datetime
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        ''' Sets and returns the string representation of the class BaseModel
        '''
        str_rep = '[' + type(self).__name__ + '] (' + self.id + ')'
        str_rep += str(self.__dict__)
        return (str_rep)

    def to_dict(self):
        ''' Returns a dictionary representation of instances of the BaseModel
            class containing only the set instance attributes.
        '''
        dict_rep = []

        if self.name is not None:
            dict_rep.append(('name', self.name))
        if self.my_number is not None:
            dict_rep.append(('my_number', self.my_number))

        others = [('__class__', type(self).__name__), ('id', self.id),
                  ('created_at', self.created_at.isoformat()),
                  ('updated_at', self.updated_at.isoformat())]
        for dic in others:
            dict_rep.append(dic)

        return dict(dict_rep)
