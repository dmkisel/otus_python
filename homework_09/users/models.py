from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class AppUser(AbstractUser):
    name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=True)
    telegram = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)

