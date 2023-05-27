from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics, permissions
from friends import serializers as friend_serializers
from accounts import serializers as account_serializers
from friends import models as friend_models

User = get_user_model()


class FriendModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self, *args, **kwargs):
        if self.action in ('list', 'retrieve'):
            return friend_serializers.FriendGetSerializer
        return friend_serializers.FriendCreateSerializer

    def get_queryset(self):
        return friend_models.Connection.objects.filter(follower=self.request.user, deleted=False)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()


class FriendSearchAPIView(generics.ListAPIView):
    serializer_class = account_serializers.UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset().exclude(id=self.request.user.id)
        username = self.request.query_params.get('username', None)
        if username:
            queryset = queryset.filter(username__icontains=username)[:10]
        return queryset[:10]
