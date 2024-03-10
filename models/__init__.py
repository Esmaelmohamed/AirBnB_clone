#!/usr/bin/python3
"""Initialization module for the models package."""
from models.engine.file_storage import FileStorage

# Create an instance of FileStorage
storage = FileStorage()

# Reload objects from the JSON file
storage.reload()

