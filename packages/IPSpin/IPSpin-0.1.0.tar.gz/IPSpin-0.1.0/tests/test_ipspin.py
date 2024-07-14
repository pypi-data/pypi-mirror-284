import unittest
from ipspin import IPSpin

class TestIPSpin(unittest.TestCase):
    def test_builder(self):
        api_key = "test_api_key"
        ipspin = IPSpin.builder(api_key)
        self.assertEqual(ipspin.config['api_key'], api_key)

if __name__ == "__main__":
    unittest.main()
