from django.contrib.auth.models import User
from django.db import models


class UserPhone(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE(),
        related_name="phone",
    )