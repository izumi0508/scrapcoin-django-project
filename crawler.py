import requests
from decimal import Decimal
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scrapcoin.settings")
django.setup()

from crypto.models import CryptoCurrency
from django.utils import timezone

class CryptoSpider:
    @staticmethod
    def script_crypto_data():
        url = 'https://api.binance.com/api/v3/ticker/price'
        response = requests.get(url)
        data = response.json()
        return data
    
    # @staticmethod
    # def script_filter_data(gt):
    #     url = 'https://api.binance.com/api/v3/ticker/price'
    #     response = requests.get(url)
    #     data = response.json()

    #     my_list = []

    #     for coin in data :
    #         if Decimal(coin["price"]) > Decimal(gt) :
    #             my_list.append(coin)

    #     return my_list
    
    @staticmethod
    def script_data_tomodel():
        url = 'https://api.binance.com/api/v3/ticker/price'
        response = requests.get(url)
        data = response.json()

        for coin in data:
            CryptoCurrency.objects.create(
                symbol = coin["symbol"],
                price = Decimal(coin["price"]),
                timestamp = timezone.now()
            )

        return response

if __name__ == "__main__":
    try:
        CryptoSpider.script_data_tomodel()
        print("資料已寫入資料庫")
    except Exception as e :
        print("程式執行失敗:", e)