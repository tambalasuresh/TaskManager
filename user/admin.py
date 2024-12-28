from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone_number','address']
    list_filter = ['name']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['id','address_line1','user','phone_number']
    list_filter = ['user']



admin.site.register(CustomUser,UserAdmin)
admin.site.register(Address,AddressAdmin)
