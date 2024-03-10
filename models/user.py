#!/usr/bin/python3
"""Module for defining the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Class representing a user entity.

    Attributes:
        email (str): The email address of the user.
        password (str): The password associated with the user account.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

