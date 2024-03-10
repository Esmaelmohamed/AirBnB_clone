#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel

class Review(BaseModel):
    """Represents a review entity.

    Attributes:
        place_id (str): The identifier of the associated place.
        user_id (str): The identifier of the user who created the review.
        text (str): The content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""

