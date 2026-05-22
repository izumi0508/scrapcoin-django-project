from rest_framework import serializers
from .models import CryptoCurrency

class CryptoCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCurrency
        fields = ['id','symbol','price','timestamp']
        