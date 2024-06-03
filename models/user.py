#!/usr/bin/python3
"""
module for User class.
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    class User for user's information
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""