import unittest

from currency_converter import app


class ConvertTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def tearDown(self):
        pass

    def test_no_parameters(self):

        result = self.client.get('/api/convert')
        self.assertEqual(result.json, dict(error='You didn\'t specify the \'amount\' parameter'))

        result = self.client.get('/api/convert?amount=100')
        self.assertEqual(result.json, dict(error='You didn\'t specify the \'from\' parameter'))

        result = self.client.get('/api/convert?amount=100&from=USD')
        self.assertEqual(result.json, dict(error='You didn\'t specify the \'to\' parameter'))

    def test_amount_no_number(self):
        result = self.client.get('/api/convert?amount=no_number')
        self.assertEqual(result.json, dict(error='Amount must be a number'))

    def test_amount_less_than_zero(self):

        error_text = 'Amount must be more than zero'

        result = self.client.get('/api/convert?amount=0')
        self.assertEqual(result.json, dict(error=error_text))

        result = self.client.get('/api/convert?amount=-100')
        self.assertEqual(result.json, dict(error=error_text))

    def test_not_available_currencies(self):

        error_text = 'Available currencies: USD, EUR, CZK, PLN'

        result = self.client.get('/api/convert?amount=100&from=USD&to=RUB')
        self.assertEqual(result.json, dict(error=error_text))

        result = self.client.get('/api/convert?amount=100&from=RUB&to=CZK')
        self.assertEqual(result.json, dict(error=error_text))

        result = self.client.get('/api/convert?amount=100&from=RUB&to=UAH')
        self.assertEqual(result.json, dict(error=error_text))

    def test_same_currency(self):
        result = self.client.get('/api/convert?amount=100&from=EUR&to=EUR')
        self.assertEqual(result.json, dict(error='You specified the same currency'))


if __name__ == '__main__':
    unittest.main()
