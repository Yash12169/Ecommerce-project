from rest_framework import serializers
from .models import Product
from tags.serializers import ReadTagsSerializer


class WriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('name','tags','description','price','quantity')

class ReadProductSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    class Meta:
        model=Product
        fields=('id','name','slug','description','price','quantity','tags')

    def get_tags(self,product):
        queryset = product.tags.all()
        return ReadTagsSerializer(queryset,many=True).data


    

    



      