from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)

    class Meta:
        verbose_name = ("message",)
        verbose_name_plural = ("messages",)
