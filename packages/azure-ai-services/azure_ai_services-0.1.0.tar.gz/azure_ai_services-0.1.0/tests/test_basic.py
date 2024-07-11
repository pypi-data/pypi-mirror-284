# tests/test_basic.py

import unittest
from azure_ai_services.basic import AzureAIBasic

class TestAzureAIBasic(unittest.TestCase):
    def setUp(self):
        self.ai = AzureAIBasic(subscription_key='fake_key', endpoint='https://fake.endpoint')

    def test_analyze_text(self):
        result = self.ai.analyze_text('Hello world')
        self.assertIn('analysis', result)

    def test_translate_text(self):
        result = self.ai.translate_text('Hello world', 'es')
        self.assertIn('translation', result)

if __name__ == '__main__':
    unittest.main()
