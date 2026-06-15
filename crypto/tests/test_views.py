from django.test import TestCase
from ..models import CryptoCurrency, CryptoKline

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

        CryptoKline.objects.create(
            symbol = 'BTCUSDT',
            interval = '1d',
            open_time = '2026-05-01T00:00:00Z',
            open_price = '100000.00',
            high_price = '100000.00',
            low_price = '100000.00',
            close_price = '100000.00',
            volume = '10'
        )

        CryptoKline.objects.create(
            symbol = 'BTCUSDT',
            interval = '1d',
            open_time = '2026-05-02T00:00:00Z',
            open_price = '100001.00',
            high_price = '100001.00',
            low_price = '100001.00',
            close_price = '100001.00',
            volume = '10'
        )

        CryptoKline.objects.create(
            symbol = 'ETHUSDT',
            interval = '1d',
            open_time = '2026-05-02T00:00:00Z',
            open_price = '5000.00',
            high_price = '5000.00',
            low_price = '5000.00',
            close_price = '5000.00',
            volume = '9'
        )

    def test_currency_api_returns_200(self):
        response = self.client.get('/api/v1/cryptos/')

        self.assertEqual(response.status_code, 200)

    def test_currency_api_filter(self):
        response = self.client.get('/api/v1/cryptos/?symbol=BTCUSDT')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['symbol'], 'BTCUSDT')

    def test_currency_api_order(self):
        response = self.client.get('/api/v1/cryptos/?ordering=-price')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['symbol'],'BTCUSDT')

    def test_kline_api_returns_200(self):
        response = self.client.get('/api/v1/klines/')

        self.assertEqual(response.status_code, 200)

    def test_kline_api_filter(self):
        response = self.client.get('/api/v1/klines/?symbol=ETHUSDT')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['symbol'], 'ETHUSDT')

    def test_kline_api_order(self):
        response = self.client.get('/api/v1/klines/?ordering=-open_time')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['symbol'],'BTCUSDT')