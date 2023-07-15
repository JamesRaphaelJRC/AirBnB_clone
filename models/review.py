#!/usr/bin/python3
''' Defines a class Review for collecting customer reviews'''
from models.base_model import BaseModel


class Review(BaseModel):
    ''' Represents the Review class

        Properties:
            place_id - the Place.id
            user_id - the User.id
            text - a customer review
    '''
    place_id = ""
    user_id = ""
    text = ""
