#!/usr/bin/python3
''' Defines a class BaseModel '''
import cmd
import uuid
from datetime import datetime


class BaseModel(cmd.Cmd):
    ''' Represents the BaseModel class '''
    def __init__(self, name, my_number):
        ''' Initializes all instances of the BaseModel class'''
        self.name = name
        self.my_number = my_number

        self.id = str(uuid.uuid4())
        created_at = datetime.now()
        updated_at = ""

    def save(self):
        ''' Updates the public instance attribute 'updated_at' with the current
            datetime
        '''
        self.updated_at = datetime.now()

    def __str__(self):
        ''' Sets the string representation of the class BaseModel'''
        str_rep = '[' + class.__name__ + '] (' + self.id + ')' + self.__dict__
        return (str_rep)

    def to_dict(self):
        ''' Returns a dictionary representation of instances of the BaseModel
            class.
        '''
        dict_rep = dict([('my_number', self.my_number), ('name', self.name),
                         ('__class__', cls.__name__), ('created_at', 

