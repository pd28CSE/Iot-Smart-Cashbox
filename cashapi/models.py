from django.db import models
import random

# Create your models here.


class ShopStore(models.Model):
    
    productcode = models.CharField(max_length=10, default=random.randint(99999, 10000000), unique=True)
    quantity = models.BigIntegerField(default=0)
    name = models.CharField(max_length=100, blank=False, null=False)
    sellingcost = models.FloatField(default=0.0)
    buyingcost = models.FloatField(default=0.0)
    
    
    def __str__(self)-> str:
        return f"{self.productcode} -> {self.name}"
     
 
 
class Customer(models.Model):
 
    productcode = models.ForeignKey(ShopStore, on_delete=models.CASCADE)
    quantity = models.BigIntegerField(default=0)
    orderdatetime = models.DateTimeField(auto_now_add=True)
    totalprice = models.FloatField(default=0.0)

    def __str__(self)-> str:
        return f"{self.productcode} -> {self.quantity}"

