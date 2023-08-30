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
    url = models.URLField()

    def __str__(self) -> str:
        return self.title


class MasterChef(models.Model):
    name = models.CharField(max_length=20)
    social = models.ForeignKey(
        SocialChef, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="uploads/chefs_images")
    details = models.TextField()

    def __str__(self) -> str:
        return self.name
