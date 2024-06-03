#!/usr/bin/python3
"""
Module for Amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an Amenity

    Attributes:
        name (str): Name of the amenity.
    """

    name = ""
