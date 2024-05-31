#!/usr/bin/python3
import uuid
import datetime

class BaseModel:
    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        pass

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance:"""
        __dict__["__class__"] = cls.__name__