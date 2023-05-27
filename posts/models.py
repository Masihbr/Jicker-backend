from django.db import models


class Post(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    text = models.TextField(max_length=140)
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        str_len = len(self.text)
        show_len = 10
        return f"{self.text[:show_len]}..." if str_len > 10 else self.text
