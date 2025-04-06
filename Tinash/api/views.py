from rest_framework import viewsets
from api.models import User, Order, Product
from .serializers import UserRegSerializer, UserLoginSerializer, UserProfileSerializer,  OrderSerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsSeller, IsBuyer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication


User = get_user_model()

class UserViewRegSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegSerializer

    def create(self, request, *args,**kwargs):
        response  = super().create(request, *args,**kwargs)
        user = User.objects.get(username=response.data['username'])
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': response.data})
        #return Response({'user':response.data })

"""class LoginUserViewSet(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    def post(self, request, *args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': {"username": user.username, "email": user.email}})
        return Response({"error": "invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
"""
class LoginUserViewSet(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': {"username": user.username, "email": user.email}})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
                            
"""
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_active:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key, 
                    'user': {
                        'username': user.username, 
                        'email': user.email,
                        'role': user.role  # Include role in response
                    }
                })
            else:
                return Response({"error": "Account is not active"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            # More detailed error message
            if not User.objects.filter(username=username).exists():
                return Response({"error": "Username does not exist"}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({"error": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)
            

class LoginUserViewSet(generics.GenericAPIView):  
    serializer_class = UserLoginSerializer  
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': {"username": user.username, "email": user.email}})
        
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
"""
class UserProfileViewSet(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    #authentication_classes = [TokenAuthentication]
    filterset_fields = ['category']
    search_fields = ['name']

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

#remember to add cart
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect('login')
