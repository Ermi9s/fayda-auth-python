import unittest
from fayda_auth.config.hosts import HostConfigManager, HostConfig

class TestHostConfigManager(unittest.TestCase):
    def test_load_from_dict(self):
        configs = {"http://example.com": "http://example.com/callback"}
        manager = HostConfigManager(configs)
        self.assertEqual(manager.get_redirect_uri("http://example.com"), "http://example.com/callback")

    def test_load_from_list(self):
        configs = [HostConfig("http://example.com", "http://example.com/callback")]
        manager = HostConfigManager(configs)
        self.assertEqual(manager.get_redirect_uri("http://example.com"), "http://example.com/callback")

    def test_add_host(self):
        manager = HostConfigManager({"http://initial.com": "http://initial.com/callback"})
        manager.add_host("http://new.com", "http://new.com/callback")
        self.assertEqual(manager.get_redirect_uri("http://new.com"), "http://new.com/callback")

    def test_remove_host(self):
        manager = HostConfigManager({"http://example.com": "http://example.com/callback"})
        manager.remove_host("http://example.com")
        self.assertIsNone(manager.get_redirect_uri("http://example.com"))

if __name__ == '__main__':
    unittest.main()