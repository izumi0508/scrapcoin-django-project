from django.test import TestCase
from ..serializers import CryptoCurrencySerializer, CryptoKlineSerializer
from ..models import CryptoCurrency, CryptoKline

class CryptoSerializerTest(TestCase):

    def test_currency_serializer_fields(self):

        coin = CryptoCurrency.objects.create(
            symbol = 'BTCUSDT',
            price = '99999.99',
            timestamp = '2026-05-01T00:00:00Z'
        )

        serializer = CryptoCurrencySerializer(coin)

        self.assertEqual(serializer.data['symbol'], 'BTCUSDT')
        self.assertIn('price', serializer.data)
        self.assertIsInstance(serializer.data['price'], str)

    def test_kline_serializer_fields(self):

        coin = CryptoKline.objects.create(
            symbol = 'BTCUSDT',
            interval = '1d',
            open_time = '2026-05-01T00:00:00Z',
            open_price = '100000.00',
            high_price = '100000.00',
            low_price = '100000.00',
            close_price = '100000.00',
            volume = '10'
        )

        serializer = CryptoKlineSerializer(coin)

        self.assertEqual(serializer.data['symbol'], 'BTCUSDT')
        self.assertIn('close_price', serializer.data)
        self.assertIsInstance(serializer.data['close_price'], str)