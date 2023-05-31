from django.contrib import admin
from .models import Product,Order
from django.contrib.auth.models import Group
from import_export.admin import ExportActionMixin
from import_export import resources
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.site_header = 'Communication Warehouse Admin Panel'

class ProductsAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ('name','category','quantity','sn')
    list_filter = ('category',)

class OrderAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ('product','staff','quantity','date','returnDate','status','extendRequested')
    list_filter = ('date',)

class UserResource(resources.ModelResource):
    class Meta:
        model = User

class UserAdmin(ExportActionMixin, UserAdmin):
    resource_class = UserResource
    pass

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# Register your models here.

admin.site.register(Product,ProductsAdmin)
admin.site.register(Order,OrderAdmin)
