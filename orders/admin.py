# orders/admin.py
# Django modules
from django.contrib import admin

# My modules
from .models import Payment, Order, OrderProduct

admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(OrderProduct)