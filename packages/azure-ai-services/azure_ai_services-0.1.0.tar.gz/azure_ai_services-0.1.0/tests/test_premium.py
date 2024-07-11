# tests/test_premium.py

import unittest
from azure_ai_services.premium import AzureAIPremium

class TestAzureAIPremium(unittest.TestCase):
    def setUp(self):
        self.ai = AzureAIPremium(subscription_key='fake_key', endpoint='https://fake.endpoint')

    def test_analyze_image(self):
        result = self.ai.analyze_image('/path/to/image.jpg')
        self.assertIn('analysis', result)

    def test_custom_model_prediction(self):
        result = self.ai.custom_model_prediction({'data': 'test'})
        self.assertIn('prediction', result)

if __name__ == '__main__':
    unittest.main()
