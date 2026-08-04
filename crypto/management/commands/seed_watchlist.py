from django.core.management.base import BaseCommand
from crypto.models import WatchList

class Command(BaseCommand):
    help = 'Populate the watchlist table'

    def handle(self, *args, **kwargs):
        created_count = 0

        symbols = [
            "ETHBTC",
            "BTCUSDT",
            "ETHUSDT",
            "BNBUSDT",
            "LTCUSDT",
            "ADAUSDT",
            "USDCUSDT",
            "SOLUSDT",
            "XRPUSDT",
            "TRXUSDT",
            "DOGEUSDT",
            "AVAXUSDT",
            "LINKUSDT",
            "USDCBNB",
            "BNBUSDC",
            "BTCUSDC",
            "ETHUSDC",
            "XRPUSDC",
            "LINKUSDC",
            "LTCUSDC",
            "ADAUSDC",
            "SOLUSDC",
            "TRXUSDC",
            "DOGEUSDC",
            "AVAXUSDC",
            "SOLBTC",
            "XRPBTC",
            "BNBBTC",
            "TRXBTC",
            "DOGEBTC",
            "ADABTC",
            "LTCBTC",
            "AVAXBTC",
            "LINKBTC",
            "SOLETH",
            "XRPETH",
            "BNBETH",
            "TRXETH",
            "ADAETH",
            "LTCETH",
            "AVAXETH",
            "LINKETH",
            "SOLBNB",
            "XRPBNB",
            "TRXBNB",
            "DOGEBNB",
            "ADABNB",
            "LTCBNB",
            "AVAXBNB",
            "LINKBNB"
        ]

        for symbol in symbols:
            obj, created =WatchList.objects.get_or_create(
                symbol=symbol,
                defaults={"is_active": True}
            )

            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(
                    f'Successfully seeded {created_count} watchlist data'
                ))