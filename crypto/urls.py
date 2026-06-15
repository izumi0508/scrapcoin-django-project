from django.urls import path
from . import views

urlpatterns = [
    path('cryptos/', views.CryptoCurrencyListView.as_view(), name='cryptos-api'),
    path('klines/', views.CryptoKlineListView.as_view(), name='cryptos-api'),
    path('test/', views.crypto_dashboard),
]