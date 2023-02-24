from rest_framework import serializers

from . models import ShopStore , Customer, OrderProduct, CustomerOrderProduct


class ShopStoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ShopStore
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = '__all__'



class OrderProductSerializer(serializers.ModelSerializer):
    productcode = ShopStoreSerializer(many=False, read_only=True)
    
    class Meta:
        model = OrderProduct
        fields = '__all__'



class CustomerOrderProductSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(many=False)
    orderproduct = OrderProductSerializer(many=True)
    
    class Meta:
        model = CustomerOrderProduct
        exclude = ['created_at', ]
        

