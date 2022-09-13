# orders/admin.py
# Django modules
from django.contrib import admin

# My modules
from .models import Payment, Order, OrderProduct


class OrderProductInLine(admin.TabularInline):
    """
    Oder product in line panel
    """
    model = OrderProduct
    readonly_fields = ("payment", "user", "product",
                        "quantity", "product_price", "ordered")
    extra = 0



class OrderAdmin(admin.ModelAdmin):
    """
    Order admin panel
    """
    list_display = ["order_number", "full_name", "phone",
                    "email", "city", "order_total",
                    "tax", "status", "is_ordered",
                    "created_at"]
    list_filter = ["status", "is_ordered"]
    search_fields = ["order_number", "first_name", "last_name"
                    "phone", "email"]
    list_per_page = 20
    inlines = [OrderProductInLine]


admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)