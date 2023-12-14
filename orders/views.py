from products.models import Product
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,RetrieveAPIView
from authentication.permissions import IsAdminUser
# Create your views here.
from django.db import transaction
class CreateOrderView(APIView):
        def compute_cost(self,orders):
            total_amount=0
            for product_id,qty in orders.items():
                try:
                 product_id = int(product_id)
                 product = Product.objects.get(pk=product_id)
                 qty = min(product.quantity,int(qty))
                 total_amount += qty*product.price
                except Product.DoesNotExist:
                    return Response("Product does not exist or is out of stock")
            return total_amount

        def post(self,request):
            orders = request.data.get('orders')
            payment_mode = request.data.get('payment_mode')
            payment_status = request.data.get('payment_status')
            user_id=request.user.id
            with transaction.atomic():
                total_amount = self.compute_cost(orders)
                
            return Response(total_amount)

class OrderDetailView(RetrieveAPIView):
    pass



class OrderListView(ListAPIView):
    pass