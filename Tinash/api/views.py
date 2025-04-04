from rest_framework import viewsets
from api.models import User, Order, Product
from .serializers import UserSerializer, OrderSerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsSeller, IsBuyer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsSeller]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    #authentication_classes = [TokenAuthentication]
    filterset_fields = ['category']
    search_fields = ['name']

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsBuyer]

#remember to add cart