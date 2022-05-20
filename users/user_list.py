from rest_framework import generics

from rest_framework.response import Response

from . import serializers


class ListUsersView(generics.RetrieveAPIView):
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user
