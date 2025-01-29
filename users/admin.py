from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_buyer', 'is_supplier']


admin.site.register(User, UserAdmin)

class tbl_registerAdmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','password','Pincode','city','address','picture')

admin.site.register(tbl_register,tbl_registerAdmin)
