#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects
    
    def new(self, obj):
        """
        Creates a new key value pair in
        the __objects dictionary
        """
        key = f"{obj.__class__.__name__}.{obj.id}" 
        self.__objects[key] = obj
    
    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        serial_objects = {}
        for key, obj in self.__objects.items():
            serial_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(serial_objects, file, indent=4)
    
    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                loaded_objs = json.load(file)
                for obj_data in loaded_objs.values():
                    class_name = obj_data.pop("__class__")
                    self.new(eval(class_name)(**obj_data))