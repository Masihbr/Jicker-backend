from django.contrib import admin
from friends import models as friend_models


@admin.register(friend_models.Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ["id", "follower", "followed", "created", "updated", "deleted"]
    list_filter = ["deleted"]
    search_fields = ["follower", "followed"]
