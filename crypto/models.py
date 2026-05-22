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
        return f"{self.symbol} @ {self.timestamp} ${self.price}"