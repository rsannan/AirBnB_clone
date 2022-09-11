#!/usr/bin/python3
"""Test BaseModel"""


from datetime import datetime
import inspect
import models
import pep8 as pycodestyle
import time
import unittest
from unittest import mock
BaseModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__


class TestBaseModelConformance(unittest.TestCase):
    """Tests for the documentation and pep8 style"""

    @classmethod
    def setUpClass(self):
        """setUp method"""
        self.base_methods = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_for_pep8(self):
        """Test for PEP8."""
        for path in ['models/base_model.py',
                     'tests/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_for_module_docstring(self):
        """Test for docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_for_class_docstring(self):
        """Test for BaseModel docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_methods_docstring(self):
        """Test for docstrings in BaseModel methods"""
        for func in self.base_methods:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""
    @mock.patch('models.storage')
    def test_for_instances(self, storage_args):
        """Test that object is created"""
        base_instance = BaseModel()
        self.assertIs(type(base_instance), BaseModel)
        base_instance.name = "Holberton"
        base_instance.number = 89
        base_attributes = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "number": int
        }
        for attr, typ in base_attributes.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, base_instance.__dict__)
                self.assertIs(type(base_instance.__dict__[attr]), typ)
        self.assertTrue(storage_args.new.called)
        self.assertEqual(base_instance.name, "Holberton")
        self.assertEqual(base_instance.number, 89)

    def test_uuid(self):
        """Test that uuid4 is valid"""
        inst_one = BaseModel()
        inst_two = BaseModel()
        for base_instance in [inst_one, inst_two]:
            uuid = base_instance.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(inst_one.id, inst_two.id)

    def test_to_dict(self):
        """Test python dict"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        d = my_model.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "Holberton")
        self.assertEqual(d['my_number'], 89)

    def test_to_dict_values(self):
        """test for correct values"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        b_model = BaseModel()
        new_d = b_model.to_dict()
        self.assertEqual(new_d["__class__"], "BaseModel")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], b_model.created_at.strftime(
            t_format
        ))
        self.assertEqual(new_d["updated_at"], b_model.updated_at.strftime(
            t_format
        ))

    def test_str(self):
        """test for the str method"""
        base_instance = BaseModel()
        string = "[BaseModel] ({}) {}".format(
            base_instance.id, base_instance.__dict__
        )
        self.assertEqual(string, str(base_instance))
