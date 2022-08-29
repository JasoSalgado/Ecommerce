# carts/admin.py
# Django modules
from django.contrib import admin
from .models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
    """
    Display in admin site
    """
    list_display = ("cart_id", "date_added")

class CartItemAdmin(admin.ModelAdmin):
    """
    Display in admin site
    """
    list_display = ("product", "cart", "quantity", "is_active")

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)