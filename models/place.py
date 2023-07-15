#!/usr/bin/python3
''' Defines a Place class'''
from models.base_model import BaseModel


class Place(BaseModel):
    ''' Represents the Place class

        Properties:
            city_id = City.id
            user_id = User.id
            name = Place name
            description = Place description
            number_rooms = Number of rooms
            number_bathrooms = Number of bathrooms
            max_guest = Maximum number of guests allowable
            price_by_night = Place price by night
            latitude = Geographical lattitude
            longitude = Geographical longitude
            amenity_ids = Amenity.id
    '''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
