from django.contrib import admin
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ( 'email', 'first_name', 'last_name','username', 'last_login', 'data_joined','is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    ordering = ('-data_joined',)


    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
# Register your models here.
admin.site.register(Account,AccountAdmin)
