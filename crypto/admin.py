from django.contrib import admin
from .models import CryptoCurrency,WatchList,CryptoKline


# Register your models here.
class CryptoCurrencyAdmin(admin.ModelAdmin):
    list_display = ("symbol", "price", "timestamp")
    list_filter = ("symbol",)
    search_fields = ("symbol",)


class WatchListAdmin(admin.ModelAdmin):
    list_display = ("symbol", "is_active")
    search_fields = ("symbol",)


class CryptoKlineAdmin(admin.ModelAdmin):
    list_display = (
        "symbol", 
        "interval", 
        "open_time", 
        "open_price", 
        "high_price", 
        "low_price", 
        "close_price", 
        "volume"
    )
    
    list_filter = ("symbol","interval",)
    search_fields = ("symbol",)


admin.site.register(CryptoCurrency,CryptoCurrencyAdmin)
admin.site.register(WatchList,WatchListAdmin)
admin.site.register(CryptoKline,CryptoKlineAdmin)