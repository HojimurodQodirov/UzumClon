from django.contrib.auth.models import User
from django.db import models


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)

    def __str__(self):
        return self.nickname
