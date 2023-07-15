#!/usr/bin/python3
''' Defines a class - User'''
from models.base_model import BaseModel


class User(BaseModel):
    ''' Represent the User class with attributes for each user

        Arguments:
            email - User's email
            password - User's password
            first_name - User's first name
            last_name - User's last name
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
