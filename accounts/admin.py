# accounts/admin.py
# Django modules
from django.contrib import admin

# My modules
from .models import Account

admin.site.register(Account)
