from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from tags.serializers import WriteTagsSerializer,ReadTagsSerializer
from django.utils.text import slugify
from .models import Tags
from django.core.cache import cache
from rest_framework.generics import RetrieveAPIView,ListAPIView,DestroyAPIView
from tags.utils import StandardResultsSetPagination
from authentication.permissions import IsAdminUser

class CreateTagView(APIView):
    permission_classes = (IsAdminUser,)
    def post(self,request):
        serializer=WriteTagsSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            tag_object=Tags.objects.create(
                name=name,
                slug=slugify(name)
            )
            json_data=ReadTagsSerializer(instance=tag_object).data
            return Response(json_data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        


class DetailTagView(APIView):
    def get(self,request,slug):
        try:
            cache_key=f"tags-{slug}"
            cached_data= cache.get(cache_key)
            if cached_data is not None:
                return Response(cached_data,status=status.HTTP_200_OK)
            tag_object=Tags.objects.get(slug=slug)
            response_data = ReadTagsSerializer(instance=tag_object)

            cache.set(cache_key,response_data)

            return Response(response_data,status=status.HTTP_200_OK)
        except Tags.DoesNotExist:
            return Response({"message":'tag not found'},status=status.HTTP_101_SWITCHING_PROTOCOLS)
        except Tags.MultipleObjectsReturned:
            return Response({"message":'multiple objects found'},status=status.HTTP_400_BAD_REQUEST)
            


class ListTagView(APIView):
    def get(self,request):
        try:
            queryset= Tags.objects.all()
            response_data= ReadTagsSerializer(instance=queryset,many=True)
            return Response(response_data,status=status.HTTP_200_OK)
        except:
            return Response({"message":"unable to fetch the tag list"},status=status.HTTP_400_BAD_REQUEST)
        



        

class DetailTagV2View(RetrieveAPIView):
    queryset=Tags.objects.all()
    serializer_class=ReadTagsSerializer
    lookup_field='slug'


class ListTagV2View(ListAPIView):
    queryset=Tags.objects.all()
    serializer_class=ReadTagsSerializer
    pagination_class=StandardResultsSetPagination


class DeleteTagView(APIView):
    def get(self,request,slug):
        try:
            tag_object=Tags.objects.get(slug=slug)
            tag_object.delete()
            return Response({"message":f"the object has been successfully deleted id {slug}"},status=status.HTTP_200_OK)
        except Tags.DoesNotExist:
            return Response({"message":'tag not found'},status=status.HTTP_101_SWITCHING_PROTOCOLS)
        except Tags.MultipleObjectsReturned:
            return Response({"message":'multiple objects found'},status=status.HTTP_400_BAD_REQUEST)

class DeleteTagV2View(DestroyAPIView):
    queryset=Tags.objects.all()
    lookup_field='slug'
    


    ##hit api for only superusers can create tags
