from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import SignUpView#,SignInView
urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('sign-in/', TokenObtainPairView.as_view(), name='sign_in'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]