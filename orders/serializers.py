from rest_framework import serializers
from .models import Orders,OrderItems
class ReadOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItems
        fields = '__all__'

class ReadOrderSerializer(serializers.Serializer):
    order_items=serializers.SerializerMethodField()
    class Meta:
        model=Orders
        fields='__all__'

    def get_order_items(self,object):
        qs = object.order_items.all()
        return ReadOrderItemSerializer(qs,many=True).data 