import unittest
from fayda_auth import FaydaAuth
from unittest.mock import Mock

class TestFaydaAuth(unittest.TestCase):
    def setUp(self):
        self.redis_mock = Mock()
        self.auth = FaydaAuth(
            redis_client=self.redis_mock,
            client_id="test_client",
            authorize_url="https://test.com/authorize",
            token_url="https://test.com/token",
            user_info_url="https://test.com/userinfo",
            private_key="dGVzdF9rZXk=",  # base64 encoded "test_key"
            client_assertion_type="test_type",
            host_configs={"http://example.com": "http://example.com/callback"}
        )

    def test_authorize(self):
        self.redis_mock.hmset.return_value = True
        self.redis_mock.expire.return_value = True
        result = self.auth.authorize("http://example.com")
        self.assertEqual(result['status_code'], 200)
        self.assertIn('auth_url', result['data'])

if __name__ == '__main__':
    unittest.main()