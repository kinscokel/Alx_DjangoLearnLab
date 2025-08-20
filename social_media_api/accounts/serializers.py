from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'bio', 'profile_picture')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password2')

        user = User.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=password,
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture')
        )
        return user
Key fixes:
password and password2 use serializers.CharField() explicitly.

User is created with User.objects.create_user() to ensure password hashing.

bio and profile_picture passed as keyword args in create_user() — this assumes your CustomUser model supports these fields in its manager, or they will be set via **kwargs in create_user() — if you want you can override create_user() in your model manager or just assign after creation.

If you don’t have a custom user manager handling bio and profile_picture, you might want to create the user with username, email, password first, then assign bio and profile_picture separately like this:

python
Copy code
def create(self, validated_data):
    password = validated_data.pop('password')
    validated_data.pop('password2')
    user = User.objects.create_user(
        username=validated_data.get('username'),
        email=validated_data.get('email'),
        password=password,
    )
    user.bio = validated_data.get('bio', '')
    user.profile_picture = validated_data.get('profile_picture')
    user.save()
    return user