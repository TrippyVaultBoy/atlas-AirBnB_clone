#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key in {"created_at", "updated_at"}:
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """
        Returns string representation of
        the current instance of the BaseModel class
        """
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance:"""
        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = self.__class__.__name__
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.updated_at.isoformat()
        return dict_obj
