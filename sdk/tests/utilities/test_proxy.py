import unittest

from lusid.utilities import format_proxy_schema


class ProxyConfigTests(unittest.TestCase):

    def test_format_schemas(self):
        proxy_config = format_proxy_schema("http://localhost:8888", "username", "password")
        expected = {
            "http": "http://username:password@localhost:8888",
            "https": "http://username:password@localhost:8888"
        }
        self.assertEqual(expected, proxy_config)
