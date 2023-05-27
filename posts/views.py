from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from posts import serializers
from posts import models as post_models

User = get_user_model()


class PostModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return post_models.Post.objects.filter(user=self.request.user, deleted=False)
    
    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()