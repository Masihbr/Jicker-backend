from django.contrib import admin
from accounts import models as account_models

# Register your models here.


@admin.register(account_models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["username"]