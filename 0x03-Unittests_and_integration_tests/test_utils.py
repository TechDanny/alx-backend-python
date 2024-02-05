#!/usr/bin/env python3
"""
Parameterize a unit test
"""


import unittest
from utils import *
from parameterized import parameterized
from typing import Dict, Mapping, Union, Sequence
from unittest.mock import Mock, patch


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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         exception: Exception) -> None:
        """
        Uses the assertRaises context manager to test that
        a KeyError is raised for the following inputs
        (use @parameterized.expand)
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Mock HTTP calls
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """
        this method is used to test that utils.get_json returns the
        expected result.
        """
        all_attributes = {"json.return_value": test_payload}

        with patch("request.get", return_value=Mock(**all_attributes)) as f:
            self.assertEqual(get_json(test_url), test_payload)
            f.assert_called_once_with(test_url)
