#!/usr/bin/python3
"""
Contains the TestAmenityDocs classes
"""


from datetime import datetime
import inspect
from models import amenity
from models.base_model import BaseModel
import pep8
import unittest
Amenity = amenity.Amenity


class TestAmenityDocs(unittest.TestCase):
    """Documentation and Pep8 Tests"""
    @classmethod
    def setUpClass(cls):
        """Set up"""
        cls.amenity_func = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance_for_amenity(self):
        """Test for PEP8 comformance"""
        pep8s = pep8.StyleGuide(quiet=True)
        res = pep8s.check_files(['models/amenity.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_amenity__docstring(self):
        """Test for docstring"""
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py needs a docstring")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py needs a docstring")

    def test_amenity_for_class_docstring(self):
        """Test for the Amenity class docstring"""
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring")

    def test_amenity_method_docstrings(self):
        """Test for docstrings in Amenity methods"""
        for func in self.amenity_func:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""
    def test_for_is_subclass_amenity_basemodel(self):
        """Tests if Amenity is a subclass of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name_attribute_present(self):
        """Test that Amenity has attribute name and\
            that it's as an empty string"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_string_output(self):
        """test if string method produces correct output"""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))
