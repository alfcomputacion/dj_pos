from django.contrib import admin

from .models import Customer

@admin.register(Customer)
class CustomAdmin(admin.ModelAdmin):
    model = Customer
