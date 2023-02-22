from django.db import models
import uuid
from django.utils import timezone
from django.utils.timezone import localtime, now

# Create your models here.


class ShopStore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.BigIntegerField(default=0)
    name = models.CharField(max_length=100, blank=False, null=False)
    sellingcost = models.FloatField(default=0.0)
    buyingcost = models.FloatField(default=0.0)
    
    
    def __str__(self)-> str:
        return "{} -> {}".format(self.name, self.id)


def getDateAndTime():
    local_time = localtime(now())
    time = str(local_time.time()).split('.')[0].replace(':', '-')
    datetime = '{}--{}'.format(local_time.date(), time)
    return datetime


class Customer(models.Model):
 
    productcode = models.ForeignKey(ShopStore, on_delete=models.CASCADE)
    quantity = models.BigIntegerField(default=0)
    orderdatetime = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(default=timezone.now()+timezone.timedelta(hours=24))
    totalprice = models.FloatField(default=0.0)

    def __str__(self)-> str:
        return f"{self.productcode} -> {self.quantity}"

