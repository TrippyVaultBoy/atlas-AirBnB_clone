#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = str(uuid.uuid4)
        self.created_at = created_at
        self.updated_at = created_at

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        pass

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance:"""
        pass