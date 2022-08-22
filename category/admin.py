# category/admin.py
# Django modules
from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    """
    Autocomplete the field slug
    """
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug') 


admin.site.register(Category, CategoryAdmin)