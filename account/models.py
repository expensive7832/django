from django.db import models
from .manager import customizeUser
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to="profile")
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = customizeUser()
