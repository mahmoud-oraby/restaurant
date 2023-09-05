from typing import Iterable, Optional
from django.db import models

# Create your models here.


class Menu(models.Model):
    TYPE_CHOSES = (
        ("B", "BREAKFAST"),
        ("L", "LAUNCH"),
        ("DI", "DINNER"),
        ("DR", "DRINK"),
    )
    title = models.CharField(max_length=50)
    type = models.CharField(choices=TYPE_CHOSES, max_length=2, blank=True)
    image = models.ImageField(upload_to="uploads/menu", blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.title


class SocialChef(models.Model):
    title = models.CharField(max_length=20)
    url = models.URLField(unique=True)

    def __str__(self) -> str:
        return f"{self.title}-{self.social.all()[0]}"


class MasterChef(models.Model):
    name = models.CharField(max_length=20)
    social = models.ManyToManyField(
        SocialChef,  related_name="social")
    image = models.ImageField(
        upload_to="uploads/chefs_images")
    details = models.TextField()
    designation = models.DateField(default="2000-1-1")

    def __str__(self) -> str:
        return self.name


class Query(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=80)
    message = models.TextField()

    def __str__(self) -> str:
        return f'{self.name}-{self.subject}'


class BookATable(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=250)
    date = models.DateTimeField()
    num_people = models.IntegerField()
    special_request = models.TextField(max_length=300)
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
