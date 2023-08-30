from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    GENDER_CHOSES = (
        ("M", "MALE"),
        ("F", "FEMALE"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    gender = models.CharField(choices=GENDER_CHOSES, max_length=1, blank=True)
    country = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='uploads/profiles_images', blank=True)
    bio = models.TextField(default="No bio")

    def __str__(self) -> str:
        return self.user.username
