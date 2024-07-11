import sys
from os import path
import unittest

sys.path.append("./")

from src.auto_switch_providers.auto_switch_providers import AutoSwitchProviders

TEMPLATE_CONFIG = {
    # "googleapi": {"http_service": {"params": {"key": ""}}},
    # "proxiesapi": {"http_service": {"params": {"auth_key": ""}}},
    "serper": {"http_service": {"headers": {"X-API-KEY": ""}}},
}

CACHE_CONFIG = {
    "host": "127.0.0.1",
    "password": "",
    "port": 6379,
    "database": "auto_switch_module:http_cached",
    "expires_in": 2592000,
}


class TestSample(unittest.TestCase):
    def test_process(self):
        response = AutoSwitchProviders(
            template_dir=f"{path.dirname(__file__)}/templates",
            config=TEMPLATE_CONFIG,
            cache_config=CACHE_CONFIG,
        ).process(
            {
                "query": "booking.com",
                "limit": 100,
                "page": 1,
                "country": "VN",
            }
        )
        self.assertEqual(response, {})


if __name__ == "__main__":
    unittest.main()
