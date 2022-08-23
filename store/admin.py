# store/admin.py
# Django modules
from django.contrib import admin

# My modules
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    """
    Display in admin site
    """
    list_display = ('product_name', 'price', 'stock',
                    'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)