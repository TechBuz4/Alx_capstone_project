from rest_framework.permissions import BasePermission
from api.models import User

class IsSeller(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and User.role == 'seller'

class IsBuyer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and User.role == 'buyer'
