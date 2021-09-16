from django.contrib.auth import get_user_model
from django.db import transaction

from .serializers import (UserCreateSerializer, UserSerializer)
from rest_framework import generics
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status, permissions

from rest_framework.settings import api_settings
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserLoginViewJWT(jwt_views.TokenObtainPairView):
    user_serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            user = User.objects.get(username=request.data[User.USERNAME_FIELD])
            serialized_user = self.user_serializer_class(user)
            response.data["data"] = {
                "user": serialized_user.data}

        return response


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (permissions.AllowAny,)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        user_token = self.get_tokens_for_user(user)
        response = {
            "success": True,
            "refresh": user_token["refresh"],
            "access": user_token["access"],
            "data": serializer.data
        }

        return Response(response, status=status.HTTP_201_CREATED, headers=headers)

    @transaction.atomic
    def perform_create(self, serializer):
        instance = serializer.save()
        return instance

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
