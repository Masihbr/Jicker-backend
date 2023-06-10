from rest_framework import serializers
from rest_framework_simplejwt.serializers import PasswordField
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = PasswordField(required=True, min_length=8)
    tokens = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ('username', 'password', 'tokens')
        read_only_fields = ('tokens',)

    def get_tokens(self, obj):
        return obj.get_tokens()

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class UserPublicProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
