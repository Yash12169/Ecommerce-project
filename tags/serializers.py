from rest_framework import serializers
from .models import Tags

class WriteTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['name']
        
class ReadTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id','name','slug','created_at']