from django.shortcuts import render
from .models import CryptoCurrency,CryptoKline
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from .serializers import CryptoCurrencySerializer,CryptoKlineSerializer
from django.shortcuts import render

# Create your views here.
# GET all items
class CryptoCurrencyListView(generics.ListAPIView):
    queryset = CryptoCurrency.objects.all()
    serializer_class = CryptoCurrencySerializer

    #filter ?ordering= ?symbol=
    filter_backends = [DjangoFilterBackend,OrderingFilter]

    filterset_fields = ['symbol']

    ordering_fields = ['symbol','price','timestamp']
    ordering = ['-timestamp']


class CryptoKlineListView(generics.ListAPIView):
    queryset = CryptoKline.objects.all()
    serializer_class = CryptoKlineSerializer

    filter_backends = [DjangoFilterBackend,OrderingFilter]

    filterset_fields = ['symbol','interval']

    ordering_fields = ['open_time', 'close_price', 'volume']
    ordering = ['-open_time', '-id']

def crypto_dashboard(request):

    context = {
        'crypto_list': CryptoKline.objects.all()
    }

    return render(request, 'crypto/index.html', context)