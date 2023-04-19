from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import validators as django_auth_validators
from django.core import validators as django_core_validators
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(
        _("username"),
        max_length=50,
        unique=True,
        help_text=_(
            "Required. Between 4 to 50 characters. Letters, digits and @/./+/-/_ only."
        ),
        validators=[django_auth_validators.UnicodeUsernameValidator(
        ), django_core_validators.MinLengthValidator(4)],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
