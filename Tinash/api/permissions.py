from rest_framework.permissions import BasePermission

class IsSeller(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'seller'

class IsBuyer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'buyer'
