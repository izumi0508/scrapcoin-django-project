from django.test import TestCase
from ..models import CryptoCurrency

class CryptoAPITest(TestCase):
    def setUp(self):
        CryptoCurrency.objects.create(
            symbol = 'BTCUSDT',
            price = '100000.00',
            timestamp = '2026-05-01T00:00:00Z'
        )

        CryptoCurrency.objects.create(
            symbol = 'ETHUSDT',
            price = '5000.00',
            timestamp = '2026-05-01T00:00:00Z'
        )

    def test_api_returns_200(self):
        response = self.client.get('/api/v1/cryptos/')

        self.assertEqual(response.status_code, 200)

    def test_api_filter(self):
        response = self.client.get('/api/v1/cryptos/?symbol=BTCUSDT')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['symbol'], 'BTCUSDT')

    def test_api_order(self):
        response = self.client.get('/api/v1/cryptos/?ordering=-price')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['symbol'],'BTCUSDT')