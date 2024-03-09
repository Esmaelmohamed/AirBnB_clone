#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the base model for the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        Args:
            *args (any): Unused.
            **kwargs (dict): Arbitrary keyword arguments.
                If provided, instance attributes are set from these arguments.
        """
        datetime_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())  # Generate unique identifier
        self.created_at = datetime.today()  # Set creation timestamp
        self.updated_at = datetime.today()  # Set last update timestamp
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, datetime_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)  # Add instance to storage

    def save(self):
        """Update last update timestamp and save the instance."""
        self.updated_at = datetime.today()  # Update last update timestamp
        models.storage.save()  # Save the instance

    def to_dict(self):
        """Return dictionary representation of the BaseModel instance.

        Returns:
            dict: Dictionary containing all instance attributes.
        """
        output_dict = self.__dict__.copy()
        output_dict["created_at"] = self.created_at.isoformat()  # Convert creation timestamp to ISO format
        output_dict["updated_at"] = self.updated_at.isoformat()  # Convert update timestamp to ISO format
        output_dict["__class__"] = self.__class__.__name__  # Add class name to dictionary
        return output_dict

    def __str__(self):
        """Return string representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
