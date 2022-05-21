import django
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework import generics
from . import serializers


class ListUsersView(generics.ListAPIView):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
