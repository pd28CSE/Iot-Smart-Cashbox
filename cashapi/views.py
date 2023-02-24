from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response

from . models import ShopStore, Customer, CustomerOrderProduct, OrderProduct
from . serializers import ShopStoreSerializer , CustomerSerializer, CustomerOrderProductSerializer

# Create your views here.


class UserDataDisplay(APIView):
    
    def get(self, request):
        shopstore = ShopStore.objects.all()
        serializer = ShopStoreSerializer(shopstore, many=True)
        
        return Response(serializer.data)



class CustomerDataDisplay(APIView):
    
    def get(self, request):
        customersProducts = CustomerOrderProduct.objects.filter(created_at__gte=timezone.now())
        serializer = CustomerOrderProductSerializer(customersProducts, many=True)
        return Response(serializer.data)
        
        
    def post(self, request):
        requestProducts = request.data
        customer = Customer.objects.create(name='user')
        customerOrderProduct = CustomerOrderProduct.objects.create(customer=customer)
        
        products = []
        totalPrice = 0
        for product in requestProducts:
            storeproduct = ShopStore.objects.get(id=product['productcode'])
            subtotal = product['quantity'] * storeproduct.sellingcost
            totalPrice += subtotal
            orderproduct = OrderProduct.objects.create(productcode=storeproduct, quantity=product['quantity'], price=subtotal)
            products.append(orderproduct)
            storeproduct.currentquantity -= product['quantity']
            storeproduct.save()
        
        customerOrderProduct.totalprice = totalPrice
        customerOrderProduct.save()

        for product in products:
            customerOrderProduct.orderproduct.add(product)
        
        products.clear()
        
        return Response({'success':'All Ok'})
        
            