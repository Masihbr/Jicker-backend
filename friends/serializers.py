from rest_framework import serializers
from friends import models as friend_models
from accounts import serializers as account_serializers


class FriendCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = friend_models.Connection
        fields = ('followed',)
    
    def validate_followed(self, value):
        if value.pk == self.context['request'].user.pk:
            raise serializers.ValidationError('You cannot follow yourself')
        if friend_models.Connection.objects.filter(
            follower=self.context['request'].user,
            followed=value,
            deleted=False,
        ).exists():
            raise serializers.ValidationError('You are already following this user')
        return value
    
    def create(self, validated_data):
        follower = self.context['request'].user
        connection = friend_models.Connection.objects.filter(
            follower=follower,
            followed=validated_data['followed'],
            deleted=True,
        ).last()
        if connection is not None:
            return super().update(connection, {'deleted': False})
        return super().create({**validated_data, 'follower': follower})


class FriendGetSerializer(serializers.ModelSerializer):
    follower = account_serializers.UserPublicProfileSerializer(
        many=False, read_only=True)
    followed = account_serializers.UserPublicProfileSerializer(
        many=False, read_only=True)

    class Meta:
        model = friend_models.Connection
        fields = ('id', 'follower', 'followed', 'created', 'updated')
        read_only_fields = ('follower',)
