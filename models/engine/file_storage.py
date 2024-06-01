#!/usr/bin/python3

import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

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
        serial_objects = {}
        for key, obj in self.__objects.items():
            serial_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file, indent=4)
    
    def reload(self):
        """
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                for obj in json.load(file).values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))