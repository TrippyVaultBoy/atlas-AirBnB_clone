#!/usr/bin/python3
import uuid
import datetime

class BaseModel:
    def __init__(self, id=None, created_at=None, updated_at=None, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        
        if kwargs is not None:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "created_at":
                    self.created_at = kwargs[key]
                elif key == "updated_at":
                    self.updated_at = kwargs[key]

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance:"""
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__