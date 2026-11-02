import requests
from decimal import Decimal
from django.core.management.base import BaseCommand
from crypto.models import CryptoKline, WatchList
from datetime import datetime, timezone

class Command(BaseCommand):
    help = 'Fetch new Crypto history kline data from Binance.'

    def handle(self, *args, **kwargs):
        DEBUG = False

        if DEBUG:
            watchlist = ["BTCUSDT","ETHUSDT"]
        else:
            watchlist = set(
                WatchList.objects.filter(is_active=True)
                .values_list("symbol", flat=True)
            )

        setinterval = '1d'

        for coin in watchlist:
            
            url = f'https://api.binance.com/api/v3/klines?symbol={coin}&interval={setinterval}&limit=1'

            try:
                response = requests.get(url,timeout=5)

                if response.status_code in [418, 429]:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Status: {response.status_code}, "
                            f"Retry-After: {response.headers.get('Retry-After')}, "
                            f"Used Weight: {response.headers.get('X-MBX-USED-WEIGHT-1M')}"
                        )
                    )
                    break
                
                response.raise_for_status()

            except requests.exceptions.RequestException as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"{coin} | {e}"
                    )
                )
                continue

            data = response.json()

            if not data:
                self.stdout.write(self.style.WARNING(f"{coin}: no data"))
                continue

            kline = data[0]
            open_time = datetime.fromtimestamp(
                kline[0] / 1000,
                tz=timezone.utc
            )

            obj, created = CryptoKline.objects.update_or_create(
                symbol = coin,
                interval = setinterval,
                open_time = open_time,
                defaults = {
                    "open_price" : Decimal(kline[1]),
                    "high_price" : Decimal(kline[2]),
                    "low_price" : Decimal(kline[3]),
                    "close_price" : Decimal(kline[4]),
                    "volume" : Decimal(kline[5]),
                }
            )

            if created:
                action = "CREATED"
            else:
                action = "UPDATED"

            self.stdout.write(
                self.style.SUCCESS(
                    f"[{action}] {coin} | {setinterval} | {open_time} | close={kline[4]}"
                )
            )
        
        self.stdout.write(self.style.SUCCESS(
            'Successfully fetch Crypto kline.'
        ))

