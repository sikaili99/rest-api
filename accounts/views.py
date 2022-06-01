from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework import generics
from accounts.models import User
from accounts.serializers import (
    Accountserializer,
    CustomTokenObtainPairSerializer,
    RefreshTokenSerializer,
    RegisterSerializer,)


class ListAccountsView(generics.ListAPIView):
    serializer_class = Accountserializer
    queryset = User.objects.all()


class EmailTokenObtainPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


class LogoutView(generics.GenericAPIView):
    serializer_class = RefreshTokenSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args):
        sz = self.get_serializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
