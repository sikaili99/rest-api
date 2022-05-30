from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from accounts.models import User


class Accountserializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
        ]

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
        username_field = User.EMAIL_FIELD
