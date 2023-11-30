from rest_framework.permissions import BasePermission,IsAuthenticated,SAFE_METHODS
from authentication.models import User
from django.conf import settings
class IsUserAuthenticated(BasePermission):
    def has_permission(self,request,view):
        return isinstance(request.user,User)
class IsActiveUser(BasePermission):
    def has_permission(self,request,view):
        return request.user.is_active == True
class IsAdminUser(BasePermission):
    def has_permission(self,request,view):
        return request.user.is_superuser == True
class ThirdPartyPermissions(BasePermission):
    def has_permission(self, request, view):
        return request.headers.get('authorization') == settings.THIRD_PARTY_TOKEN
        return True
    