#!/usr/bin/python3
import uuid
from datetime import date, datetime

class BaseModel():
    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid.uuid4)
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        pass

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance:"""
        pass