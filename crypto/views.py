from django.shortcuts import render
from .models import CryptoCurrency
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from .serializers import CryptoCurrencySerializer

# Create your views here.
# GET all items
class CryptoCurrencyListView(generics.ListAPIView):
    queryset = CryptoCurrency.objects.all()
    serializer_class = CryptoCurrencySerializer

    #filter ?ordering= ?symbol=
    filter_backends = [DjangoFilterBackend,OrderingFilter]

    filterset_fields = ['symbol']

    ordering_fields = ['id','symbol','price','timestamp']
    ordering = ['-timestamp']


def crypto_dashboard(request):

    context = {
        'crypto_list': CryptoCurrency.objects.all()
    }

    return render(request, 'crypto/index.html', context)
    
# # GET a single item by ID
# class MyDetailView(generics.RetrieveAPIView):
#     queryset = MyModel.objects.all()
#     serializer_class = MySerializer