from django.test import TestCase
from ..serializers import CryptoCurrencySerializer
from ..models import CryptoCurrency

class CryptoSerializerTest(TestCase):

    def test_serializer_fields(self):

        coin = CryptoCurrency.objects.create(
            symbol = 'BTCUSDT',
            price = '99999.99',
            timestamp = '2026-05-01T00:00:00Z'
        )

        serializer = CryptoCurrencySerializer(coin)

        self.assertEqual(serializer.data['symbol'], 'BTCUSDT')
        self.assertIn('price', serializer.data)
        self.assertIsInstance(serializer.data['price'], str)