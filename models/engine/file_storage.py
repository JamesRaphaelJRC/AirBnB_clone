#!/usr/bin/python3
''' Defines a class FileStorage '''
import json
from models.base_model import BaseModel


class FileStorage:
    ''' Represents the class - FileStorage

        Attributes:
            __file_path: The name of the file to save objects
            __objects: A dictionary of instantiated objects
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' Returns a dictionary of all objects of a class '''
        return FileStorage.__objects

    def new(self, obj):
        ''' Sets a key 'class name>.id' and value 'obj' to the __objects
            dictionary
        '''
        obj_cls_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_cls_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path
            
            obj_dict = A dictionary containing all objects in this format:
            <class_name>.id Eg "BaseModel.1234556: {'name': 'First Model'}"
            results in {"Basemodel.1234556": "{'name': 'first model'}"} before being serialized
        """
        dicted = {}
        obj_dict = FileStorage.__objects
        for key in obj_dict.keys():
            dicted[key] = obj_dict[key].to_dict()

        with open(FileStorage.__file_path, "w") as JsonFile:
            json.dump(dicted, JsonFile) # Serializes dicted & write its content to the JsonFile

    def reload(self):
        ''' De-serializes the JSON file to __objects if the JSON file
            (__file_path) exists, otherwise nothing is done
        '''
        try:
            with open(FileStorage.__file_path) as JsonFile:
                obj_dict = json.load(JsonFile)
                for obj in obj_dict.values():
                    if isinstance(obj, dict) and "__class__" in obj:
                        cls_name = obj["__class__"] # Extracts the class name
                        del obj["__class__"] # deletes the class key from the dictionary
                        self.new(eval(cls_name)(**obj)) # **obj passes the remaining key-value pairs
        except FileNotFoundError:
            return
