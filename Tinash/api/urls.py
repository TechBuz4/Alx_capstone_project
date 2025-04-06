"""from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewRegSet,LoginUserViewSet,UserProfileViewSet,  ProductViewSet, OrderViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
#router.register(r'register', UserViewRegSet, basename='register')
#router.register(r'login', LoginUserViewSet, basename='login')
#router.register(r'profile', UserProfileViewSet, basename='profile')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('api/', include(router.urls)),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', UserViewRegSet.as_view(), name='register'),
    path('api/login/', LoginUserViewSet.as_view(), name='login'),
    path('api/profile/', UserProfileViewSet.as_view(), name='profile'),

]
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewRegSet,
    LoginUserViewSet,
    UserProfileViewSet,
    ProductViewSet,
    OrderViewSet
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', UserViewRegSet.as_view(), name='register'),
    path('api/login/', LoginUserViewSet.as_view(), name='login'),
    path('api/profile/', UserProfileViewSet.as_view(), name='profile'),
]
