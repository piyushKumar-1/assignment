from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from django.contrib.auth import authenticate
import re

class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, email):
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not email or not re.search(email_regex,email):
            raise ValidationError("Please Use a valid email address!")
        if User.objects.filter(username=email).exists():
            raise ValidationError("User with this email already exist.")
        return email

    def validate_password(self, password):
        if not password:
            raise ValidationError("Password is required!")
        return password

    def validate_name(self, name):
        if not name:
            raise ValidationError("First name is required!")
        return name



    def create(self, validated_data):
        email, password, name = validated_data['email'], validated_data['password'], validated_data['name']
        obj = User.objects.create_user(email=email, username=email, password=password, first_name=name)
        return obj


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if not data['email'] or not data['password']:
            raise ValidationError("Both fields are required!")
        if not User.objects.filter(username=data['email']):
            raise AuthenticationFailed("No such user found")
        user = authenticate(username=data['email'], password=data['password'])
        if user and user.is_active:
            return user
        raise AuthenticationFailed("Incorrect Credentials")
