from django.contrib import admin
from posts import models as post_models


@admin.register(post_models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "text", "created", "updated", "deleted"]
    list_filter = ["deleted"]
    search_fields = ["user"]
