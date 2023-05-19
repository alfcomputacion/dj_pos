from django.contrib import admin

from .models import Sale, SaleDetail

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    model = Sale

@admin.register(SaleDetail)
class SaleDetailAdmin(admin.ModelAdmin):
    model = SaleDetail