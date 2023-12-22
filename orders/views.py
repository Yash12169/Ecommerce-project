from products.models import Product
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,RetrieveAPIView
from authentication.permissions import IsAdminUser
from .models import Orders,OrderItems
from rest_framework import status
from .serializers import ReadOrderSerializer
from django.db import transaction
class CreateOrderView(APIView):
        def post(self,request):
            orders = request.data.get('orders')
            payment_mode = request.data.get('payment_mode')
            payment_status = request.data.get('payment_status')
            user_id=request.user.id
            with transaction.atomic():
                order = Orders.objects.create(
                    user_id=user_id,
                    payment_mode=payment_mode,
                    payment_status=payment_status,
                    payment_amount=0
                )
                total_amount=0
                for product_id,qty in orders.items():
                     product_id=int(product_id)
                     product = Product.objects.create()
                     qty = min(int(product.quantity),int(qty))
                     total_amount += product.price * qty
                     OrderItems.objects.create(
                          product_id=product_id,

                          ## resolve error and hit API request
                          order_id=order.id,
                          price=product.price,
                          quantity=qty
                     )
                order.payment_amount=total_amount
                order.save()

            response_data=ReadOrderSerializer(instance=orders).data
            return Response(response_data,status=status.HTTP_200_OK)

class OrderDetailView(RetrieveAPIView):
    pass

class OrderListView(ListAPIView):
    pass