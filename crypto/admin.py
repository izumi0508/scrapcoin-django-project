from django.contrib import admin
from .models import CryptoCurrency

# Register your models here.
class CryptoCurrencyAdmin(admin.ModelAdmin):
    list_display = ("symbol", "price", "timestamp")

admin.site.register(CryptoCurrency,CryptoCurrencyAdmin)
