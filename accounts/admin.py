# accounts/admin.py
# Django modules
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# My modules
from .models import Account

class AccountAdmin(UserAdmin):
    """
    Modify the account admin
    """
    # Properties that will be displayed in the admin site
    list_display = ('email', 'first_name', 'last_name', 
                    'username', 'last_login', 'date_joined', 
                    'is_active')
    # If user clicks on a particular column will redirect to the properties
    list_display_link = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    


admin.site.register(Account, AccountAdmin)


