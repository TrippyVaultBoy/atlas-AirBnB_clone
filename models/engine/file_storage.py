#!/usr/bin/python3

import json

class FileStorage:
    def __init__(self, file_path, objects):
        self.__file_path = file_path
        self.__objects = objects
    
    def all(self):
        return self.__objects
    
    def new(self, obj):
        """
        Creates a new key value pair in
        the __objects dictionary
        """
        key = f"{obj.__class__.__name__}.{obj.id}" 
        self.__objects[key] = obj
    
    def save(self):
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file, indent=4)
    
    def reload(self):
        """
        """
        if self.__file_path != None:
            data = json.loads(self.__file_path)
            self.__objects.update(data)