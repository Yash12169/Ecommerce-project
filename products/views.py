from django.shortcuts import render
from rest_framework.views import APIView
from authentication.permissions import IsAdminUser
from .serializers import WriteProductSerializer,ReadProductSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Product
from django.utils.text import slugify
from tags.utils import StandardResultsSetPagination
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class CreateProductView(APIView):
    permission_classes = (IsAdminUser,)

    def post(self,request):
        serializer = WriteProductSerializer(data= request.data)
        if serializer.is_valid():
            product = Product.objects.create(
                name=serializer.validated_data.get('name'),
                slug=slugify(serializer.validated_data.get('name')),
                price=serializer.validated_data.get('price'),
                quantity=serializer.validated_data.get('quantity'),
                description=serializer.validated_data.get('description'),
            )
            product.tags.set(serializer.validated_data.get('tags'))
            return Response({"message":"product is created"},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class DetailProductView(RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ReadProductSerializer
    lookup_field="slug"


class ListProductView(ListAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Product.objects.all()
    serializer_class = ReadProductSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['^name','description'] # first it searches for name then description
    ordering_fields = ['id','created_at']
    filterset_fields=['id','tags']