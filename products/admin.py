from django.contrib import admin


from .models import Category, Product

# admin.site.register(Category)
# admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product