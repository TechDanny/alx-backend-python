#!/usr/bin/env python3
"""
Parameterize a unit test
"""


import unittest
from utils import *
from parameterized import parameterized
from typing import Dict, Mapping, Union, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests the methods
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),

    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Union[Dict, int]) -> None:
        """
         tests that the method returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
