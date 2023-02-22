from django.contrib import admin

from . models import ShopStore, Customer

# Register your models here.

admin.site.register(ShopStore)
admin.site.register(Customer)