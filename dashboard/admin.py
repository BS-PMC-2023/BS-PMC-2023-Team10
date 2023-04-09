from django.contrib import admin
from .models import Product,Order


admin.site.site_header = 'Communication Warehouse Admin Panel'

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name','category','quantity','Serial Number')
    list_filter = ('category',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product','staff','quantity','date')
    list_filter = ('date',)


admin.site.register(Product,ProductsAdmin)
admin.site.register(Order,OrderAdmin)
