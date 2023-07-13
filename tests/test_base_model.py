#!/usr/bin/python3
"""Defines unittests for models"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class TestBaseModel_instant(unittest.TestCase):
    """Test for instantiation of the BaseModel class"""

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel())

    def test_new_instance_stored(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_uids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_created_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_updated_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str_rep(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.-__str__()
        self.assertin("[BaseModel] (123456)", bmstr)
        self.assertin("'id': '123456'", bmstr)
        self.assertin("'created_at':" + dt_repr, bmstr)
        self.assertin("'updated_at':" + dt_repr, bmstr)
