import requests
from decimal import Decimal
from django.core.management.base import BaseCommand
from crypto.models import CryptoCurrency, WatchList
from django.utils import timezone

class Command(BaseCommand):
    help = 'Fetch new Crypto history datas from Binance to the database'

    def handle(self, *args, **kwargs):
        url = 'https://api.binance.com/api/v3/ticker/price'
        response = requests.get(url)
        data = response.json()
        now = timezone.now()

        watchlist = set(
            WatchList.objects.filter(is_active=True)
            .values_list("symbol", flat=True)
        )

        for coin in data:

            if coin["symbol"] not in watchlist:
                continue
            
            CryptoCurrency.objects.update_or_create(
                symbol = coin["symbol"],
                timestamp = now,
                defaults = {
                    "price" : Decimal(coin["price"])
                }
            )
        
        self.stdout.write(self.style.SUCCESS(
            'Successfully fetch new Crypto history datas to the database'
        ))
