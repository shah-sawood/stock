from django.contrib import admin

from .models import Purchase, Portfolio, History

# Register your models here.
@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    readonly_fields = ["symbol", "name"]


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    pass


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    pass
