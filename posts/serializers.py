from rest_framework import serializers
from posts import models as post_models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = post_models.Post
        fields = ('id', 'user', 'text', 'created', 'updated')
        read_only_fields = ('user',)
        
    def create(self, validated_data):
        return super().create({**validated_data, 'user': self.context['request'].user})
