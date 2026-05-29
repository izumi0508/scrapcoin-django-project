from django.test import TestCase
from ..models import CryptoCurrency

class CryptoModelTest(TestCase):

    def test_string_representation(self):

        coin = CryptoCurrency.objects.create(
            symbol='BTCUSDT',
            price='100000.00',
            timestamp='2026-05-01T00:00:00Z'
        )

        self.assertIn('BTCUSDT', str(coin))