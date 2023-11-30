from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListAPIView
from .serializers import ReadUserSerializer
from .permissions import IsAdminUser
from .authentication import ThirdPartyAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .utils import CustomRateThrottle
class SignUpView(APIView):
    def post(self,request):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        if not username:
            return Response({"error": True, "msg" : "Username is required"},status=status.HTTP_400_BAD_REQUEST)
        if not email:
            return Response({"error": True, "msg" : "Email is required"},status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response({"error": True, "msg" : "Password is required"},status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({"error": True, "msg" : "User already exists"},status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({"error": True, "msg" : "email already exists"},status=status.HTTP_400_BAD_REQUEST)
        User.objects.create_user(username=username, email=email, password=password)
        user = auth.authenticate(username=username, password=password)
        if user:
            return Response({"success": True, "msg" : "User is created"},status=status.HTTP_200_OK)
        else:
            return Response({"error": True, "msg" : "something went wrong"},status=status.HTTP_400_BAD_REQUEST)

class UserListView(ListAPIView):
    authentication_classes = (ThirdPartyAuthentication,JWTAuthentication,)
    permission_classes = (IsAdminUser,)
    serializer_class = ReadUserSerializer
    throttle_classes = (CustomRateThrottle,)
    def get_queryset(self):
        queryset = User.objects.all()   
        return queryset
        
        
