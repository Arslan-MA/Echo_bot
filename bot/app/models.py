from django.contrib.auth.models import User
from django.db import models


class UserMessage(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.message


class BotMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.message
