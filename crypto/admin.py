from django.contrib import admin
from .models import CryptoCurrency,WatchList

# Register your models here.
class CryptoCurrencyAdmin(admin.ModelAdmin):
    list_display = ("symbol", "price", "timestamp")
    list_filter = ("symbol",)
    search_fields = ("symbol",)

class WatchListAdmin(admin.ModelAdmin):
    list_display = ("symbol", "is_active")
    search_fields = ("symbol",)

admin.site.register(CryptoCurrency,CryptoCurrencyAdmin)
admin.site.register(WatchList,WatchListAdmin)