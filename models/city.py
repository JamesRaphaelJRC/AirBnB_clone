#!/usr/bin/python3
''' Defines a city class.'''
from models.base_model import BaseModel


class City(BaseModel):
    ''' Defines the City class'

        Properties:
            state_id - the State.id
            name - The state name
    '''
    state_id = ""
    name = ""
