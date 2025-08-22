from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()      # <--- exactly like this
    password2 = serializers.CharField()     # <--- exactly like this

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'password2', 'bio', 'profile_picture')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password2')

        user = get_user_model().objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=password,
        )
        user.bio = validated_data.get('bio', '')
        user.profile_picture = validated_data.get('profile_picture')
        user.save()

        Token.objects.create(user=user)

        return user

from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']