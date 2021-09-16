from rest_framework import serializers

from django.core import exceptions
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", 'email', 'password', "username", "first_name", "last_name")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ("id", 'email', 'password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        exclude = ["password"]
