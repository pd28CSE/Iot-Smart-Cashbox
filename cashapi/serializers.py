from rest_framework import serializers

from . models import ShopStore, Customer


class ShopStoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ShopStore
        fields = '__all__'




class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = '__all__'
