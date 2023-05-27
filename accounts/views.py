from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from accounts import serializers

User = get_user_model()


class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = serializers.UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
