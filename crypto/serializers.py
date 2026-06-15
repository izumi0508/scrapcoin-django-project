from rest_framework import serializers
from .models import CryptoCurrency, CryptoKline


class CryptoCurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = CryptoCurrency
        fields = ['id','symbol','price','timestamp']


class CryptoKlineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CryptoKline
        fields = [
            'id',
            'symbol',
            'interval',
            'open_time',
            'open_price',
            'high_price',
            'low_price',
            'close_price',
            'volume'
        ]
        ordering = ['open_time']