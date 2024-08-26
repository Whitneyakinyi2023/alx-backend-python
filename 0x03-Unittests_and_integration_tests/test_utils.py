#!/usr/bin/env python3
"""test_utils.py"""


import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the access_nested_map function."""

    @parameterized.expand([
        # Test cases with valid paths
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that access_nested_map returns the expected result.

        Parameters:
        nested_map (dict): The nested map to test.
        path (tuple): The path to access in the nested map.
        expected (any): The expected value at the given path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        # Test cases that should raise a KeyError
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that KeyError is raised with the appropriate message.

        Parameters:
        nested_map (dict): The nested map to test.
        path (tuple): The path to access in the nested map.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        # Check if the exception message is as expected
        self.assertEqual(str(cm.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    """Test cases for the get_json function."""

    @parameterized.expand([
        # Test cases with different URLs and payloads
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that get_json returns the expected result.

        Parameters:
        test_url (str): The URL to fetch JSON from.
        test_payload (dict): The expected payload from the URL.
        """
        with patch('utils.requests.get') as mocked_get:
            # Mock the response to return the test_payload
            mocked_response = Mock()
            mocked_response.json.return_value = test_payload
            mocked_get.return_value = mocked_response

            response = get_json(test_url)
            # Ensure the get method was called with the correct URL
            mocked_get.assert_called_once_with(test_url)
            # Ensure the returned JSON matches the expected payload
            self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """Test cases for the memoize decorator."""

    def test_memoize(self):
        """
        Test that a_property is memoized correctly.

        Checks that a_method is called only once and the result is cached.
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mocked_method:
            test_instance = TestClass()
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Ensure a_method was called only once
            mocked_method.assert_called_once()
            # Ensure the correct value is returned from the property
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == "__main__":
    unittest.main()
