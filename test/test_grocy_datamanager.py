from unittest import TestCase
from unittest.mock import patch, mock_open
import unittest


from typing import List
import responses
from pygrocydm import GrocyDataManager
from pygrocydm.product import Product
from pygrocydm.chore import Chore

from test.test_const import CONST_BASE_URL, CONST_PORT, CONST_SSL, SKIP_REAL


class TestGrocyDataManager(TestCase):

    def setUp(self):
        self.gdm = GrocyDataManager(CONST_BASE_URL, "api_key")
        self.gdm = None
        self.gdm = GrocyDataManager(CONST_BASE_URL, "demo_mode",  verify_ssl = CONST_SSL, port = CONST_PORT)

    def test_init(self):
        assert isinstance(self.gdm, GrocyDataManager)

    def test_products(self):
        products = self.gdm.products()
        assert isinstance(products, list)
        assert len(products) >=1
        for product in products:
            assert isinstance(product, Product)

    def test_chores(self):
        chores = self.gdm.chores()
        assert isinstance(chores, list)
        assert len(chores) >=1
        for chore in chores:
            assert isinstance(chore, Chore)
