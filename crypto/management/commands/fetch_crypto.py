import requests
from decimal import Decimal
from django.core.management.base import BaseCommand
from crypto.models import CryptoCurrency
from django.utils import timezone

class Command(BaseCommand):
    help = 'Fetch new Crypto history datas from Binance to the database'

    def handle(self, *args, **kwargs):
        url = 'https://api.binance.com/api/v3/ticker/price'
        response = requests.get(url)
        data = response.json()

        for coin in data:
            CryptoCurrency.objects.create(
                symbol = coin["symbol"],
                price = Decimal(coin["price"]),
                timestamp = timezone.now()
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully fetch new Crypto history datas to the database'))
