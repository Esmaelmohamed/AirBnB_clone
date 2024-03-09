import json

class FileStorage:
    """A class for storing data in a JSON file."""

    def __init__(self, file_path):
        """
        Initialize FileStorage with the given file path.

        Args:
            file_path (str): The path to the JSON file.
        """
        self.file_path = file_path
        self.data = {}

    def save(self):
        """
        Save the current data to the JSON file.
        """
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file)

    def load(self):
        """
        Load data from the JSON file into the data dictionary.
        """
        try:
            with open(self.file_path, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            # Handle the case where the file doesn't exist
            self.data = {}

    def set_item(self, key, value):
        """
        Set a key-value pair in the data dictionary.

        Args:
            key: The key for the item.
            value: The value to be stored.
        """
        self.data[key] = value

    def get_item(self, key):
        """
        Retrieve the value associated with the given key from the data dictionary.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        return self.data.get(key)

    def remove_item(self, key):
        """
        Remove an item from the data dictionary based on the key.

        Args:
            key: The key of the item to remove.
        """
        if key in self.data:
            del self.data[key]

    def reload(self):
        """
        Reload data from the JSON file into the data dictionary.
        """
        try:
            with open(self.file_path, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            # Handle the case where the file doesn't exist
            self.data = {}
