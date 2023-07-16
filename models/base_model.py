#!/usr/bin/python3
''' Defines a class BaseModel '''
import uuid
from datetime import datetime
import models


class BaseModel:
    ''' Represents the BaseModel class '''
    def __init__(self, *args, **kwargs):
        ''' Initializes an instance of the BaseModel class'''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.fromisoformat(value)
                elif key == 'updated_at':
                    self.updated_at = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
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
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def to_dict(self):
        ''' Returns a dictionary representation of instances of the BaseModel
            class containing only the set instance attributes.
        '''
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = type(self).__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return (dict_rep)
