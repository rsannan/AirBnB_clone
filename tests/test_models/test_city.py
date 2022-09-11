#!/usr/bin/python3
"""
Contains tests for the TestCity class
"""


from datetime import datetime
import inspect
from models import city
from models.base_model import BaseModel
import pep8
import unittest
City = city.City


class TestCityConformance(unittest.TestCase):
    """Tests for documentations and pep8 style"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.city_func = inspect.getmembers(City, inspect.isfunction)

    def test_for_pep8_conformance_city_class(self):
        """Test that models/city.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_for_pep8_conformance_test_city_class(self):
        """Test that tests/test_city.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_for_city_module_docstring(self):
        """Test for the city.py module docstring"""
        self.assertIsNot(city.__doc__, None,
                         "city.py needs a docstring")
        self.assertTrue(len(city.__doc__) >= 1,
                        "city.py needs a docstring")

    def test_for_class_city_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(City.__doc__, None,
                         "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class needs a docstring")

    def test_city_methods_docstring(self):
        """Test for docstrings in City class methods"""
        for func in self.city_func:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestCity(unittest.TestCase):
    """Test the City class"""
    def test_city_is_subclass_model(self):
        """Test that City is a subclass of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_for_name_attribute(self):
        """Test that City has attribute name, and it's an empty string"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")

    def test_for_state_id_attribute(self):
        """Test that City has attribute state_id, and it's an empty string"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")

    def test_for_to_dict(self):
        """test to_dict method"""
        c = City()
        new_dict = c.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attr in c.__dict__:
            self.assertTrue(attr in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_for_to_dict_values(self):
        """test for values in dict"""
        iso_t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = City()
        new_dict = c.to_dict()
        self.assertEqual(new_dict["__class__"], "City")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], c.created_at.strftime(
            iso_t_format
        ))
        self.assertEqual(new_dict["updated_at"], c.updated_at.strftime(
            iso_t_format
        ))

    def test_str(self):
        """test that the str method has the correct output"""
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))
