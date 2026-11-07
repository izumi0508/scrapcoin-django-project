from django.db import models


# Create your models here.
class CryptoCurrency(models.Model):
    symbol = models.CharField(max_length = 50)
    price = models.DecimalField(max_digits = 20, decimal_places = 8)
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ["symbol", "timestamp"]
        indexes = [
            models.Index(fields=["symbol", "timestamp"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields = ["symbol", "timestamp"],
                name = "unique_symbol_timestamp"
            )
        ]

    def __str__(self):
        return self.symbol


class WatchList(models.Model):
    symbol = models.CharField(max_length = 50, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["symbol"]

    def __str__(self):
        return self.symbol


class CryptoKline(models.Model):
    symbol = models.CharField(max_length = 20)
    interval = models.CharField(max_length=10)

    open_time = models.DateTimeField()

    open_price = models.DecimalField(max_digits = 20, decimal_places = 8)
    high_price = models.DecimalField(max_digits = 20, decimal_places = 8)
    low_price = models.DecimalField(max_digits = 20, decimal_places = 8)
    close_price = models.DecimalField(max_digits = 20, decimal_places = 8)

    volume = models.DecimalField(max_digits = 20, decimal_places = 8)

    class Meta:
        ordering = ["symbol", "interval", "-open_time", "-id"]

        indexes = [
            models.Index(fields=["symbol", "interval", "open_time"]),
        ]

        constraints = [
            models.UniqueConstraint(
                fields = ["symbol", "interval", "open_time"],
                name = "unique_symbol_interval_open_time"
            )
        ]

    def __str__(self):
        return self.symbol