# store/admin.py
# Django modules
import admin_thumbnails
from django.contrib import admin

# My modules
from .models import Product, ReviewRating, Variation, ProductGallery

@admin_thumbnails.thumbnail("image")
class ProductGalleryInLine(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    """
    Display in admin site
    """
    list_display = ('product_name', 'price', 'stock',
                    'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInLine]

class VariationAdmin(admin.ModelAdmin):
    """
    Display in admin site
    """
    list_display = ('product', 'variation_category', 'variation_value',
                    'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value',
                    'is_active')


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)
