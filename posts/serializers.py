from rest_framework import serializers
from posts import models as post_models
from accounts import serializers as account_serializers


class PostSerializer(serializers.ModelSerializer):
    user = account_serializers.UserPublicProfileSerializer(many=False, read_only=True)
    
    class Meta:
        model = post_models.Post
        fields = ('id', 'user', 'text', 'created', 'updated')
        
    def create(self, validated_data):
        return super().create({**validated_data, 'user': self.context['request'].user})
