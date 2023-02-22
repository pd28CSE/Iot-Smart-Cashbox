from rest_framework.views import APIView
from rest_framework.response import Response

from . models import ShopStore, Customer
from . serializers import ShopStoreSerializer, CustomerSerializer

# Create your views here.


class UserDataDisplay(APIView):
    
    def get(self, request):
        shopstore = ShopStore.objects.all()
        serializer = ShopStoreSerializer(shopstore, many=True)
        
        return Response(serializer.data)



class CustomerDataDisplay(APIView):
    
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
        
        
    def post(self, request):
        data = request.data
        product = ShopStore.objects.get(id=data['productcode'])
        
        data["totalprice"] = int(data['quantity']) * product.sellingcost
        
        customerserializer = CustomerSerializer(data=data)
        if customerserializer.is_valid():
            customerserializer.save()
            product.quantity = product.quantity - data['quantity']
            product.save()
            
            return Response(customerserializer.data)
        
        return Response(customerserializer.errors)
            