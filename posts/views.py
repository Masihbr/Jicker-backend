from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics, permissions
from posts import serializers
from posts import models as post_models
from friends import models as friends_models
from rest_framework.pagination import LimitOffsetPagination

User = get_user_model()


class PostModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return post_models.Post.objects.filter(user=self.request.user, deleted=False)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()


class TimelineListAPIView(generics.ListAPIView):
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        friends = friends_models.Connection.objects.filter(
            follower=self.request.user, deleted=False).values_list('followed', flat=True)
        return post_models.Post.objects.filter(user__in=friends, deleted=False)
