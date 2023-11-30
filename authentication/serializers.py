from rest_framework.serializers import ModelSerializer
from .models import User


class ReadUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','is_active','is_superuser')


