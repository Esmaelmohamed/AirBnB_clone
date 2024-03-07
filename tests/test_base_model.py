import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_id_generation(self):
        # Check if the id is a string
        self.assertIsInstance(self.base_model.id, str)
        # Check if the length of the id is 36 characters
        self.assertEqual(len(self.base_model.id), 36)

    def test_created_at(self):
        # Check if created_at is a datetime object
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        # Check if updated_at is a datetime object
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_method(self):
        # Save the current updated_at value
        prev_updated_at = self.base_model.updated_at
        # Call the save method
        self.base_model.save()
        # Check if updated_at has been updated
        self.assertNotEqual(prev_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        # Convert the BaseModel instance to a dictionary
        obj_dict = self.base_model.to_dict()
        # Check if '__class__' key exists
        self.assertIn('__class__', obj_dict)
        # Check if 'created_at' key exists
        self.assertIn('created_at', obj_dict)
        # Check if 'updated_at' key exists
        self.assertIn('updated_at', obj_dict)
        # Check if 'id' key exists
        self.assertIn('id', obj_dict)

if __name__ == '__main__':
    unittest.main()
