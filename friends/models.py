from django.db import models
from django.core.exceptions import ValidationError


class Connection(models.Model):
    follower = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE, related_name="follower_set")
    followed = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE, related_name="followed_set")
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('follower', 'followed')

    def __str__(self):
        return f"{self.followed} is followed by {self.follower}"

    def clean(self):
        super().clean()
        if self.follower.pk == self.followed.pk:
            raise ValidationError('Follower and followed can\'t be the same')
