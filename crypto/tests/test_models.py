from django.test import TestCase
from django.db import IntegrityError
from ..models import CryptoCurrency, WatchList, CryptoKline

class CryptoModelTest(TestCase):

    def test_currency_string_representation(self):

        coin = CryptoCurrency.objects.create(
            symbol = 'BTCUSDT',
            price = '100000.00',
            timestamp = '2026-05-01T00:00:00Z'
        )

        self.assertEqual(str(coin), 'BTCUSDT')

    def test_watchlist_string_representation(self):

        coin = WatchList.objects.create(
            symbol = 'BTCUSDT',
            is_active = True
        )

        self.assertEqual(str(coin), 'BTCUSDT')

    #不能重複追蹤同一個幣
    def test_watchlist_unique_constraint(self):

        WatchList.objects.create(symbol = 'BTCUSDT')

        with self.assertRaises(IntegrityError):
            WatchList.objects.create(symbol = 'BTCUSDT')

    def test_watchlist_default_is_active(self):

        coin = WatchList.objects.create(symbol='ETHUSDT')

        self.assertTrue(coin.is_active)

    def test_kline_string_representation(self):

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

        self.assertEqual(str(coin), 'BTCUSDT')