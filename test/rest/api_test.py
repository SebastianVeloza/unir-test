import http.client
import os
import unittest
from urllib.request import urlopen

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/3/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    def test_api_multiply_invalid(self):
        url = f"{BASE_URL}/calc/multiply/3/a"
        with self.assertRaises(Exception):
            urlopen(url, timeout=DEFAULT_TIMEOUT)

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/6/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/6/0"
        with self.assertRaises(Exception):
            urlopen(url, timeout=DEFAULT_TIMEOUT)

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    def test_api_power_invalid(self):
        url = f"{BASE_URL}/calc/power/a/3"
        with self.assertRaises(Exception):
            urlopen(url, timeout=DEFAULT_TIMEOUT)

    def test_api_sqrt_valid(self):
        url = f"{BASE_URL}/calc/sqrt/16"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    def test_api_sqrt_invalid(self):
        url = f"{BASE_URL}/calc/sqrt/-1"
        with self.assertRaises(Exception):
            urlopen(url, timeout=DEFAULT_TIMEOUT)

    def test_api_log10_valid(self):
        url = f"{BASE_URL}/calc/log10/1000"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    def test_api_log10_invalid(self):
        url = f"{BASE_URL}/calc/log10/0"
        with self.assertRaises(Exception):
            urlopen(url, timeout=DEFAULT_TIMEOUT)
