from django.shortcuts import render
from rest_framework import generics, permissions, status
from .serializers import UserSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings



class LoginAPI(generics.GenericAPIView):
  serializer_class = LoginSerializer
  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    refresh = RefreshToken.for_user(user)
    token = str(refresh)
    return Response({
        'user_id':user.id,
        'JWT access token':token,
        'JWT refresh token':token
        },
    status=status.HTTP_200_OK
    )


class CreateUserAPIView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    def post(self, request):
        user = request.data
        serializer = self.get_serializer(data=user)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        token = str(refresh)
        return Response({
            'user_id':user.id,
            'JWT access token':token,
            'JWT refresh token':token
            },
        status=status.HTTP_200_OK
        )
