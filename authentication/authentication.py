from rest_framework import authentication
from .models import User
from rest_framework_simplejwt.tokens import AccessToken
from django.conf import settings
class ThirdPartyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        if request.headers.get('Authorization') == settings.THIRD_PARTY_TOKEN :
            third_party_user = User(
                is_superuser = True,
                is_active = True
            )
            return (third_party_user,None)
        else:
            return None