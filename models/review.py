#!/usr/bin/python3
"""
Module for Review class.
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    Represents a Review

    Attributes:
        place_id (str): The Place ID.
        user_id (str): The User ID.
        text (str): The text of the review.
    """

place_id = ""
user_id = ""
text = ""