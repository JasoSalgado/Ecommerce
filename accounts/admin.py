# accounts/admin.py
# Django modules
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

# My modules
from .models import Account, UserProfile

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
    

class UserProfileAdmin(admin.ModelAdmin):
    """
    User profile admin
    """
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;>'.format(object.profile_picture.url))
    
    thumbnail.short_description = "Imagen de perfil"
    list_display = ("thumbnail", "user", "city",
                    "state", "country")


admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)


