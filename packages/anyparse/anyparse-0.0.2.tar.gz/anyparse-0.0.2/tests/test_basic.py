import unittest

from loguru import logger

from src.anyparse import anyparse


class TestBasic(unittest.TestCase):
    def setUp(self):
        logger.info("init testing...")

    def test_foo(self):
        result = anyparse.parse("a:1, b:2", ["a"], ",")
        self.assertEqual({'a': '1'}, result)
