from django.contrib import admin

from . models import ShopStore , Customer, OrderProduct, CustomerOrderProduct

# Register your models here.


class ShopStoreAdmin(admin.ModelAdmin):
    model = ShopStore
    fields = ['name', 'brand', 'quantity', 'sellingcost', 'buyingcost', 'currentquantity']
    list_display = ['name', 'brand', 'id', 'quantity', 'sellingcost', 'buyingcost', 'currentquantity']

admin.site.register(ShopStore, ShopStoreAdmin)

admin.site.register(Customer)
admin.site.register(OrderProduct)
admin.site.register(CustomerOrderProduct)