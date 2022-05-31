from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from accounts.models import User
from accounts.serializers import (
    Accountserializer,
    CustomTokenObtainPairSerializer,
    RegisterSerializer,)


class ListAccountsView(generics.ListAPIView):
    serializer_class = Accountserializer
    queryset = User.objects.all()


class EmailTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny, ]
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
